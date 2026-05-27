import numpy as np

def get_support_resistance(df, window=20):
    """
    Simple intraday support/resistance detection
    """

    recent = df.tail(window)

    support = recent["low"].min()
    resistance = recent["high"].max()

    return support, resistance


def is_breakout(price, resistance):
    return price > resistance * 1.001  # small buffer


def is_breakdown(price, support):
    return price < support * 0.999