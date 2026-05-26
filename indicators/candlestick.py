def detect_candle(df):
    latest = df.iloc[-1]

    body = abs(latest["close"] - latest["open"])
    candle_range = latest["high"] - latest["low"]

    if body < candle_range * 0.1:
        return "DOJI"

    if latest["close"] > latest["open"]:
        return "BULLISH"

    return "BEARISH"