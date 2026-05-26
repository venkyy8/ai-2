from candlestick.patterns import *

def detect_all(candles):
    latest = candles.iloc[-1]
    previous = candles.iloc[-2]

    patterns = []

    if detect_doji(latest.Open, latest.Close, latest.High, latest.Low):
        patterns.append("DOJI")

    if detect_marubozu(latest.Open, latest.Close, latest.High, latest.Low):
        patterns.append("MARUBOZU")

    if detect_hammer(latest.Open, latest.Close, latest.High, latest.Low):
        patterns.append("HAMMER")

    if detect_bullish_engulfing(
        previous.Open, previous.Close,
        latest.Open, latest.Close
    ):
        patterns.append("BULLISH_ENGULFING")

    return patterns
