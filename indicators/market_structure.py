import numpy as np

def detect_structure(df, lookback=5):
    """
    Detect HH, HL, LH, LL structure (simple version)
    """

    highs = df["high"].tail(lookback).values
    lows = df["low"].tail(lookback).values

    trend = "SIDEWAYS"

    # Higher Highs + Higher Lows → Uptrend
    if highs[-1] > highs[-2] and lows[-1] > lows[-2]:
        trend = "UPTREND"

    # Lower Highs + Lower Lows → Downtrend
    elif highs[-1] < highs[-2] and lows[-1] < lows[-2]:
        trend = "DOWNTREND"

    return trend