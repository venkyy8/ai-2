
import pandas as pd

def add_features(df):
    df = df.copy()

    df["returns"] = df["close"].pct_change()
    df["sma_5"] = df["close"].rolling(5).mean()
    df["sma_10"] = df["close"].rolling(10).mean()

    df["trend"] = (df["sma_5"] > df["sma_10"]).astype(int)

    df.dropna(inplace=True)
    return df
