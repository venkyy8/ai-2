import yfinance as yf


def get_market_data(symbol, interval="5m", period="5d"):
    df = yf.download(
        tickers=symbol,
        interval=interval,
        period=period,
        progress=False
    )

    if df.empty:
        return None

    df = df.reset_index()

    df.columns = [str(col).lower() for col in df.columns]

    return df