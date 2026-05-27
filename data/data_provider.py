import yfinance as yf
import pandas as pd


def get_market_data(symbol, interval="5m", period="7d"):

    try:
        df = yf.download(
            tickers=symbol,
            interval=interval,
            period=period,
            progress=False,
            auto_adjust=False,
            group_by="column"
        )

        if df is None or df.empty:
            return None

        # 🧠 FIX: flatten multi-index columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [col[0] for col in df.columns]

        # convert to lowercase safely
        df.columns = [str(col).lower() for col in df.columns]

        required = ["open", "high", "low", "close", "volume"]

        if not all(col in df.columns for col in required):
            return None

        df = df.reset_index()

        return df

    except Exception as e:
        print(f"Data error for {symbol}: {e}")
        return None
