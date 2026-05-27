def generate_signal(rsi, ema_fast, ema_slow, volume_spike, trend_signal):

    # STRONG BUY SETUP
    if trend_signal == "BULLISH_CONFIRM":
        if rsi > 50 and volume_spike:
            return "BUY", 85

    # STRONG SELL SETUP
    if trend_signal == "BEARISH_CONFIRM":
        if rsi < 50:
            return "SELL", 85

    return "WAIT", 40