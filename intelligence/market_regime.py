def detect_regime(df):

    atr = (df["high"] - df["low"]).mean()
    trend = df["close"].iloc[-1] - df["close"].iloc[-10]

    if atr > 10 and abs(trend) > 20:
        return "VOLATILE"

    if trend > 0:
        return "TRENDING_UP"

    if trend < 0:
        return "TRENDING_DOWN"

    return "RANGE"