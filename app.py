from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
import requests
import time
import os

app = Flask(__name__)

# Define prometheus metrics
crypto_request_counter = Counter('crypto_request_count', 'Number of cryptocurrency API requests')
crypto_request_duration = Gauge('crypto_request_duration_seconds', 'Duration of cryptocurrency API requests')

crypto_price_gauges = {}

api_key = os.getenv('API_KEY')

if not api_key:
    raise ValueError("API_KEY is not in environment variables.")

@app.route('/')
def get_crypto_data():
    start_time = time.time()
    crypto_request_counter.inc()

    headers = { 'X-CMC_PRO_API_KEY': api_key, 'Accepts': 'application/json' }
    params = { 'start': '1', 'limit': '5', 'convert': 'USD' }
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    try:
        # Make request to Coinmarketcap API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  

        data = response.json()
        coins = data['data']
        
        for coin in coins:
            crypto_name = coin['name']
            crypto_price = coin['quote']['USD']['price']
            
            if crypto_name not in crypto_price_gauges:
                crypto_price_gauges[crypto_name] = Gauge(
                    f'crypto_price_{crypto_name.lower().replace(" ", "_")}',
                    f'Price of {crypto_name} in USD'
                )
            
            crypto_price_gauges[crypto_name].set(crypto_price)

        return 'Successfully exposed metrics for top 5 crypto'

    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error retrieving data: {e}")
        return 'Error retrieving data'

    finally:
        duration = time.time() - start_time
        crypto_request_duration.set(duration)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

