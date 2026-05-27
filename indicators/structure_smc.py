def detect_bos(df):
    """
    Break of Structure (simple version)
    """

    if len(df) < 5:
        return "NO_DATA"

    last = df.iloc[-1]
    prev_high = df["high"].iloc[-5]
    prev_low = df["low"].iloc[-5]

    if last["close"] > prev_high:
        return "BULLISH_BOS"

    if last["close"] < prev_low:
        return "BEARISH_BOS"

    return "NO_BOS"