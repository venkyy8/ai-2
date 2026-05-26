import yfinance as yf
import pandas as pd


def get_market_data(symbol="RELIANCE.NS", interval="5m", period="5d"):

    df = yf.download(
        tickers=symbol,
        interval=interval,
        period=period,
        progress=False,
        threads=False
    )

    if df is None or df.empty:
        return None

    df = df.reset_index()

    df.rename(columns={
        "Datetime": "timestamp",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    }, inplace=True)

    return df
