from intelligence.confidence_engine import calculate_confidence


def generate_signal(rsi, ema_fast, ema_slow, volume_spike):
    confidence = calculate_confidence(
        rsi,
        ema_fast,
        ema_slow,
        volume_spike
    )

    if confidence >= 75:
        return "BUY", confidence

    if confidence <= 25:
        return "SELL", confidence

    return "WAIT", confidence