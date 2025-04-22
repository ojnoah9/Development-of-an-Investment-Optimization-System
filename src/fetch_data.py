# src/fetch_data.py
import yfinance as yf
import pandas as pd

# Fetch historical data from Yahoo Finance
def get_data(tickers, start="2020-01-01", end="2024-12-31"):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)  # auto_adjust set to True by default
    data = data.dropna()  # Drop any rows with NaN values
    data.to_csv("data/historical_data.csv")
    return data
