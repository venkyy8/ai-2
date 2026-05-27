def adapt_confidence(base_confidence, sentiment, performance):

    confidence = base_confidence

    # sentiment adjustment
    if sentiment == "BULLISH":
        confidence += 5

    elif sentiment == "BEARISH":
        confidence -= 5

    # performance adjustment
    if performance > 60:
        confidence += 5
    elif performance < 40:
        confidence -= 5

    return max(0, min(100, confidence))