def calculate_confidence(rsi, ema_fast, ema_slow, volume_spike):
    score = 0

    if 50 < rsi < 70:
        score += 25

    if ema_fast > ema_slow:
        score += 25

    if volume_spike:
        score += 25

    if rsi > 55:
        score += 25

    return score