import yfinance as yf
import pandas as pd


def get_market_data(symbol="RELIANCE.NS", interval="5m", period="5d"):
    """
    Fetch intraday market data (FREE)
    """

    print(f"📡 Fetching live data for {symbol}...")

    df = yf.download(
        tickers=symbol,
        interval=interval,
        period=period,
        progress=False
    )

    if df.empty:
        print("❌ No data received")
        return None

    df = df.reset_index()

    # Standardize column names for your pipeline
    df.rename(columns={
        "Datetime": "timestamp",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    }, inplace=True)

    print("✅ Data fetched successfully")

    return df
