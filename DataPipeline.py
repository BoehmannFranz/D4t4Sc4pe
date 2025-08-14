import pandas as pd
import time
from datetime import datetime
import numpy as np
import requests

# Liste der Top-KI-Unternehmen (Beispiele)
TICKERS = ["GOOGL", "NVDA", "AAPL", "TSLA", "MSFT"]
import os
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Please set the ALPHAVANTAGE_API_KEY environment variable.")

def fetch_stock_prices(tickers):
    prices = {}
    for ticker in tickers:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
            price = float(data["Global Quote"]["05. price"])
            prices[ticker] = round(price, 3)
        except Exception as e:
            print(f"Warning: Could not fetch {ticker}, using dummy value. {e}")
            prices[ticker] = round(np.random.uniform(100, 500), 3)  # more realistic values
        time.sleep(12)  # Alpha Vantage erlaubt nur 5 Requests pro Minute (kostenlos)
    return prices

def create_stock_dataframe(num_rows=40, sleep_time=1):
    columns = ["Index", "Timestamp"] + TICKERS
    df = pd.DataFrame(columns=columns)
    for idx in range(num_rows):
        prices = fetch_stock_prices(TICKERS)
        timestamp = datetime.now()
        row = [idx, timestamp] + [prices[ticker] for ticker in TICKERS]
        df.loc[len(df)] = row
        print(df.tail(1))
        time.sleep(sleep_time)
    # Save DataFrame as CSV
    df.to_csv("AI Stock Model 1.csv", index=False)
    return df

# Example for direct call (can be removed when used only as import)
if __name__ == "__main__":
    df = create_stock_dataframe()
    print(df.head())