import time

from data.data_provider import get_market_data
from features.feature_engine import add_features as create_features
from candlestick.detector import detect_all
from strategy.signal_engine import generate_signal


print("🚀 AI Trader V2 Started (50-Stock Intraday Scanner)")


# ===============================
# 50 STOCK INTRADAY WATCHLIST
# ===============================
WATCHLIST = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "SBIN.NS", "BHARTIARTL.NS", "ITC.NS", "LT.NS", "KOTAKBANK.NS",

    "AXISBANK.NS", "INDUSINDBK.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS",
    "FEDERALBNK.NS", "PNB.NS", "BANKBARODA.NS", "IDFCFIRSTB.NS",

    "WIPRO.NS", "HCLTECH.NS", "TECHM.NS", "LTIM.NS", "PERSISTENT.NS",

    "MARUTI.NS", "TATAMOTORS.NS", "M&M.NS", "EICHERMOT.NS", "BAJAJ-AUTO.NS",

    "TATASTEEL.NS", "JSWSTEEL.NS", "HINDALCO.NS", "JINDALSTEL.NS", "VEDL.NS",

    "ONGC.NS", "IOC.NS", "BPCL.NS", "COALINDIA.NS",

    "SUNPHARMA.NS", "DRREDDY.NS", "CIPLA.NS", "DIVISLAB.NS",

    "HINDUNILVR.NS", "NESTLEIND.NS", "BRITANNIA.NS", "DABUR.NS",

    "ADANIENT.NS", "ADANIPORTS.NS", "LTTS.NS", "IDEA.NS", "ZOMATO.NS",
    "PAYTM.NS", "NYKAA.NS"
]


INTERVAL = "5m"
PERIOD = "5d"


# ===============================
# PROCESS SINGLE STOCK
# ===============================
def process_stock(symbol):

    try:
        print(f"\n📡 Scanning: {symbol}")

        df = get_market_data(
            symbol=symbol,
            interval=INTERVAL,
            period=PERIOD
        )

        if df is None or df.empty:
            print(f"❌ No data: {symbol}")
            return None

        # Feature engineering
        df = create_features(df)

        # Candlestick detection
        df = detect_all(df)

        # Signal generation
        signal = generate_signal(df)

        print(f"📊 {symbol} → {signal}")

        return {
            "symbol": symbol,
            "signal": signal
        }

    except Exception as e:
        print(f"⚠️ Error processing {symbol}: {e}")
        return None


# ===============================
# MAIN EXECUTION
# ===============================
if __name__ == "__main__":

    print("\n🔥 Running 50-Stock AI Intraday Scanner...\n")

    results = []
    buy_candidates = []

    for stock in WATCHLIST:
        result = process_stock(stock)

        if result:
            results.append(result)

            # OPTIONAL: filter BUY signals
            if "BUY" in str(result["signal"]).upper():
                buy_candidates.append(result)

        # small delay to avoid API overload
        time.sleep(0.5)

    # ===============================
    # FINAL REPORT
    # ===============================
    print("\n==============================")
    print("📈 FINAL AI MARKET SCAN REPORT")
    print("==============================")

    for r in results:
        print(f"{r['symbol']} → {r['signal']}")

    print("\n==============================")
    print("🔥 TOP BUY CANDIDATES")
    print("==============================")

    if buy_candidates:
        for b in buy_candidates:
            print(f"🚀 {b['symbol']} → {b['signal']}")
    else:
        print("No strong BUY signals found")

    print("\n✅ Scan Complete\n")

