from config import STOCKS, INTERVAL, PERIOD
from data.data_provider import get_market_data
from features.feature_engine import add_features
from strategy.signal_engine import generate_signal


def process_stock(symbol):

    df = get_market_data(symbol, INTERVAL, PERIOD)

    if df is None or df.empty:
        return None

    df = add_features(df)
    latest = df.iloc[-1]

    signal, score = generate_signal(
        latest["rsi"],
        latest["ema_fast"],
        latest["ema_slow"],
        latest["volume_spike"]
    )

    if signal == "HOLD":
        return None

    return {
        "symbol": symbol,
        "signal": signal,
        "score": score,
        "price": latest["close"]
    }


def scan():

    buys = []
    sells = []

    print("\n==============================")
    print("🔥 AI TRADE SCANNER")
    print("==============================")

    for stock in STOCKS:

        result = process_stock(stock)

        if result:
            if result["signal"] == "BUY":
                buys.append(result)
            else:
                sells.append(result)

    # ---------------- TOP FILTER (IMPORTANT)
    buys = sorted(buys, key=lambda x: x["score"], reverse=True)[:5]
    sells = sorted(sells, key=lambda x: x["score"])[:5]

    print("\n🔥 TOP BUY OPPORTUNITIES")
    print("==============================")

    for b in buys:
        print(f"{b['symbol']} | BUY | ₹{b['price']} | Score: {b['score']}")

    print("\n🔻 TOP SELL OPPORTUNITIES")
    print("==============================")

    for s in sells:
        print(f"{s['symbol']} | SELL | ₹{s['price']} | Score: {s['score']}")

    if not buys and not sells:
        print("No strong opportunities right now")

    print("\n✅ Scan Complete\n")


if __name__ == "__main__":
    scan()
