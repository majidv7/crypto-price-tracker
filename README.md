# Crypto Price Tracker

A Flask-based application that fetches top 5 cryptocurrency data (prices) from the Coinmarketcap API and exposes metrics for Prometheus & Grafana.

## Usage

1. **Clone the Repository:**
    ```
    git clone https://github.com/majidv7/crypto-price-tracker.git
    cd crypto-price-tracker
    ```

2. **Start the App with Docker Compose:**
    ```
    docker-compose up -d
    ```    

3. **Check the app status:**
    
The app will now be accessible at [http://localhost:5000](http://localhost:3000).

4. **Now head to the Grafan Dashboard and add your desired metrics:**

[http://localhost:5000](http://localhost:5000).


---

## Requirements

Before running the application, ensure you have the following:

1. **Coinmarketcap API Key:**
   - Visit [Coinmarketcap Pro](https://pro.coinmarketcap.com).
   - Obtain your API key.

2. **Update Environment in .env File:**
   - Open the `.env` file in the project root.
   - Add your Coinmarketcap API key and set your desired Grafana password:

        ```
        API_KEY=your_coinmarketcap_api_key
        GF_ADMIN_PASS=your_desired_grafana_password
        ```

Make sure to keep your API key and Grafana admin password secure.
