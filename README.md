# Crypto Price Tracker

A Flask-based application that fetches top 5 cryptocurrency prices from the CoinMarketCap API and exposes metrics for Prometheus & Grafana monitoring.

---

## Usage

1. **Clone the Repository:**
    ```
    git clone https://github.com/majidv7/crypto-price-tracker.git
    cd crypto-price-tracker
    ```

2. **Set up environment variables:**

    Create your environment file from the example:

    ```
    cp .env.example .env
    ```

    Then update it with your own values:

    ```
    API_KEY=your_coinmarketcap_api_key
    GF_ADMIN_PASS=your_desired_grafana_password
    ```   

3. **Start the App with Docker Compose:**
    ```
    docker-compose up -d
    ```

4. **Check the App Status:**

   The application will be available at:

   http://localhost:5000

5. **Grafana Dashboard:**

   Open Grafana to visualize metrics:

   http://localhost:3000

   Default login:
   - Username: admin
   - Password: (value from GF_ADMIN_PASS)

---

## Requirements

Before running the application, ensure you have the following:

1. **CoinMarketCap API Key:**
   - Visit [CoinMarketCap Pro](https://pro.coinmarketcap.com)
   - Create an account and generate an API key

2. **Docker Installed:**
   - Docker
   - Docker Compose

3. **Environment Configuration:**
   - Create a `.env` file in the project root
   - Add required variables:

    ```
    API_KEY=your_coinmarketcap_api_key
    GF_ADMIN_PASS=your_desired_grafana_password
    ```

---

## Notes

- Keep your API key and Grafana credentials secure
- This project is intended for personal learning and observability practice (Prometheus + Grafana)
