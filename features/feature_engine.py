import pandas as pd

def add_features(df):
    df = df.copy()

    # ---------------- EMA (trend)
    df["ema_fast"] = df["close"].ewm(span=9, adjust=False).mean()
    df["ema_slow"] = df["close"].ewm(span=21, adjust=False).mean()

    # ---------------- RSI (proper + stable)
    delta = df["close"].diff()

    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()

    rs = gain / loss
    df["rsi"] = 100 - (100 / (1 + rs))

    # ---------------- Volume spike (realistic)
    df["volume_spike"] = df["volume"] > (df["volume"].rolling(20).mean() * 1.2)

    # ---------------- Clean
    df.dropna(inplace=True)

    return df
