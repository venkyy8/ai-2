def smc_decision(bos, price, support, resistance):

    # Stop hunt near resistance → SELL opportunity
    if price > resistance and bos == "BEARISH_BOS":
        return "SELL", 90

    # Stop hunt near support → BUY opportunity
    if price < support and bos == "BULLISH_BOS":
        return "BUY", 90

    # Breakout continuation
    if bos == "BULLISH_BOS":
        return "BUY", 75

    if bos == "BEARISH_BOS":
        return "SELL", 75

    return "WAIT", 40