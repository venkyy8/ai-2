from config import STOCKS, INTERVAL, PERIOD

from data.data_provider import get_market_data
from indicators.technicals import add_indicators
from indicators.candlestick import detect_candle

from indicators.liquidity import detect_liquidity_zones
from indicators.structure_smc import detect_bos
from intelligence.smc_engine import smc_decision

from intelligence.news_sentiment import get_news_sentiment
from intelligence.market_regime import detect_regime

from learning.memory import save_trade, get_success_rate

from intelligence.adaptive_engine import adapt_confidence
from intelligence.risk_engine import calculate_levels


def scan():

    buy_list = []
    sell_list = []

    performance = get_success_rate()

    for symbol in STOCKS:

        try:
            df = get_market_data(symbol, INTERVAL, PERIOD)

            if df is None or df.empty:
                continue

            df = add_indicators(df)
            latest = df.iloc[-1]

            price = latest["close"]

            # =========================
            # PHASE 4: STRUCTURE
            # =========================
            support, resistance = detect_liquidity_zones(df)
            bos = detect_bos(df)

            signal, base_confidence = smc_decision(
                bos,
                price,
                support,
                resistance
            )

            # =========================
            # PHASE 6: AI LAYERS
            # =========================
            sentiment = get_news_sentiment(symbol)
            regime = detect_regime(df)

            confidence = adapt_confidence(
                base_confidence,
                sentiment,
                performance
            )

            # regime filter (important)
            if regime == "VOLATILE":
                confidence -= 10

            sl, target = calculate_levels(price)

            result = {
                "symbol": symbol,
                "price": price,
                "signal": signal,
                "confidence": confidence,

                "support": support,
                "resistance": resistance,
                "bos": bos,

                "sentiment": sentiment,
                "regime": regime,
                "performance": performance,

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

    # =========================
    # OUTPUT
    # =========================
    print("\n==============================")
    print("🔥 PHASE 6 - AI TRADING ENGINE")
    print("==============================")

    if not buy_list and not sell_list:
        print("No BUY/SELL opportunities right now")
        return

    if buy_list:

        print("\n========== BUY ==========")
        for t in buy_list:
            print(
                f"{t['symbol']} | ₹{t['price']:.2f} | "
                f"CONF: {t['confidence']:.2f}% | "
                f"BOS: {t['bos']} | "
                f"Sent: {t['sentiment']} | "
                f"Regime: {t['regime']}"
            )

    if sell_list:

        print("\n========== SELL ==========")
        for t in sell_list:
            print(
                f"{t['symbol']} | ₹{t['price']:.2f} | "
                f"CONF: {t['confidence']:.2f}% | "
                f"BOS: {t['bos']} | "
                f"Sent: {t['sentiment']} | "
                f"Regime: {t['regime']}"
            )

    print("\n==============================")
    print(f"TOTAL BUY: {len(buy_list)} | TOTAL SELL: {len(sell_list)}")
    print(f"SYSTEM WIN RATE: {performance:.2f}%")
    print("==============================\n")


if __name__ == "__main__":
    scan()