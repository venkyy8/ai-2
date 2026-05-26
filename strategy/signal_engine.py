def generate_signal(patterns, rsi, ema_fast, ema_slow, volume_spike):

    score = 0

    if "MARUBOZU" in patterns:
        score += 25

    if "BULLISH_ENGULFING" in patterns:
        score += 30

    if rsi < 35:
        score += 20

    if ema_fast > ema_slow:
        score += 15

    if volume_spike:
        score += 10

    if score >= 70:
        return "STRONG BUY"

    elif score >= 50:
        return "BUY"

    elif score >= 30:
        return "WATCH"

    return "NO TRADE"
