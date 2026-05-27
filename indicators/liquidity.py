import numpy as np

def detect_liquidity_zones(df, window=20):

    highs = df["high"].rolling(window).max()
    lows = df["low"].rolling(window).min()

    resistance_zone = highs.iloc[-1]
    support_zone = lows.iloc[-1]

    return support_zone, resistance_zone