def generate_signal(rsi, ema_fast, ema_slow, volume_spike):

    score = 50
    ema_diff = ema_fast - ema_slow

    # ---------------- RSI filter (stronger)
    if rsi < 30:
        score += 20
    elif rsi > 70:
        score -= 25
    elif 45 <= rsi <= 55:
        score += 5

    # ---------------- Trend filter (important)
    if ema_diff > 0:
        score += 15
    else:
        score -= 20

    # ---------------- Volume confirmation (soft)
    if volume_spike:
        score += 10

    # ---------------- FINAL DECISION (stricter)
    if score >= 75:
        return "BUY", score
    elif score <= 30:
        return "SELL", score
    else:
        return "HOLD", score
