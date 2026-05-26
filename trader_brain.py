def validate_trade(signal, market_trend, volatility):

    if market_trend == "SIDEWAYS":
        return "SKIP"

    if volatility > 3:
        return "RISKY"

    return signal
