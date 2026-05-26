from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator


def add_indicators(df):
    df["rsi"] = RSIIndicator(df["close"]).rsi()
    df["ema_fast"] = EMAIndicator(df["close"], window=9).ema_indicator()
    df["ema_slow"] = EMAIndicator(df["close"], window=21).ema_indicator()

    df["volume_avg"] = df["volume"].rolling(20).mean()
    df["volume_spike"] = df["volume"] > df["volume_avg"]

    return df