def get_sentiment(symbol):

    # simple proxy logic (Phase 5 starter)
    # later upgrade with news + twitter + API

    bullish_stocks = ["RELIANCE", "TCS", "INFY", "HDFCBANK"]
    bearish_stocks = ["IDEA", "YESBANK"]

    if any(s in symbol for s in bullish_stocks):
        return "BULLISH"

    if any(s in symbol for s in bearish_stocks):
        return "BEARISH"

    return "NEUTRAL"