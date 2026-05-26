from candlestick.patterns import *


def detect_all(candles):
    candles = candles.copy()

    # normalize column names (IMPORTANT FIX)
    candles.columns = [col.lower() for col in candles.columns]

    latest = candles.iloc[-1]
    previous = candles.iloc[-2]

    patterns = []

    # DOJI
    if detect_doji(latest["open"], latest["close"], latest["high"], latest["low"]):
        patterns.append("DOJI")

    # MARUBOZU
    if detect_marubozu(latest["open"], latest["close"], latest["high"], latest["low"]):
        patterns.append("MARUBOZU")

    # HAMMER
    if detect_hammer(latest["open"], latest["close"], latest["high"], latest["low"]):
        patterns.append("HAMMER")

    # BULLISH ENGULFING
    if detect_bullish_engulfing(
        previous["open"], previous["close"],
        latest["open"], latest["close"]
    ):
        patterns.append("BULLISH_ENGULFING")

    # attach result to dataframe (VERY IMPORTANT)
    candles["patterns"] = ", ".join(patterns) if patterns else "NONE"

    return candles
