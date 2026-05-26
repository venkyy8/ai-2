def detect_doji(open_, close, high, low):
    body = abs(close - open_)
    candle_range = high - low
    return body <= candle_range * 0.1


def detect_marubozu(open_, close, high, low):
    body = abs(close - open_)
    wick = (high - max(open_, close)) + (min(open_, close) - low)
    return wick < body * 0.1


def detect_hammer(open_, close, high, low):
    body = abs(close - open_)
    lower_shadow = min(open_, close) - low
    return lower_shadow > body * 2


def detect_bullish_engulfing(prev_open, prev_close, open_, close):
    return prev_close < prev_open and close > open_ and close > prev_open
