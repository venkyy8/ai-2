from config import STOCKS, INTERVAL, PERIOD
from data.data_provider import get_market_data
from indicators.technicals import add_indicators
from indicators.candlestick import detect_candle
from intelligence.decision_engine import generate_signal
from intelligence.risk_engine import calculate_levels
from learning.memory import save_trade


def scan():
    buy_list = []
    sell_list = []

    for symbol in STOCKS:
        try:
            df = get_market_data(symbol, INTERVAL, PERIOD)

            if df is None:
                continue

            df = add_indicators(df)

            latest = df.iloc[-1]

            signal, confidence = generate_signal(
                latest["rsi"],
                latest["ema_fast"],
                latest["ema_slow"],
                latest["volume_spike"]
            )

            price = latest["close"]
            sl, target = calculate_levels(price)

            result = {
                "symbol": symbol,
                "signal": signal,
                "confidence": confidence,
                "price": price,
                "sl": sl,
                "target": target,
                "candle": detect_candle(df)
            }

            save_trade(result)

            if signal == "BUY":
                buy_list.append(result)

            elif signal == "SELL":
                sell_list.append(result)

        except Exception:
            continue

    print("\n========== BUY SIGNALS ==========")
    for stock in buy_list:
        print(
            f"{stock['symbol']} | "
            f"₹{stock['price']:.2f} | "
            f"Confidence: {stock['confidence']}% | "
            f"SL: ₹{stock['sl']} | "
            f"Target: ₹{stock['target']}"
        )

    print("\n========== SELL SIGNALS ==========")
    for stock in sell_list:
        print(
            f"{stock['symbol']} | "
            f"₹{stock['price']:.2f} | "
            f"Confidence: {stock['confidence']}%"
        )


if __name__ == "__main__":
    scan()