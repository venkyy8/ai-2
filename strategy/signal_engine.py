import pandas as pd


def generate_signal(df):
    """
    Simple intraday signal engine
    """

    df = df.copy()

    close = df["close"]

    # Indicators
    rsi = compute_rsi(close)
    ema_fast = close.ewm(span=9).mean()
    ema_slow = close.ewm(span=21).mean()

    volume_spike = 0
    if "volume" in df.columns:
        volume_spike = df["volume"].pct_change().iloc[-1]

    # Latest values
    rsi_val = rsi.iloc[-1]
    ema_fast_val = ema_fast.iloc[-1]
    ema_slow_val = ema_slow.iloc[-1]

    # SIGNAL LOGIC
    if rsi_val < 30 and ema_fast_val > ema_slow_val:
        return "BUY"

    elif rsi_val > 70 and ema_fast_val < ema_slow_val:
        return "SELL"

    else:
        return "HOLD"


def compute_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()

    rs = gain / loss
    return 100 - (100 / (1 + rs))
