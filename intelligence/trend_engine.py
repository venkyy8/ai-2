def trend_confirmation(trend, ema_fast, ema_slow):
    
    if trend == "UPTREND" and ema_fast > ema_slow:
        return "BULLISH_CONFIRM"

    if trend == "DOWNTREND" and ema_fast < ema_slow:
        return "BEARISH_CONFIRM"

    return "NO_CONFIRM"