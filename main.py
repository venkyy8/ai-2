import time

from data.data_provider import get_market_data
from features.feature_engine import add_features as create_features
from candlestick.detector import detect_all
from strategy.signal_engine import generate_signal


print("🚀 AI Trader Started (CLEAN SIGNAL MODE)")


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

    "ADANIENT.NS", "ADANIPORTS.NS", "LTTS.NS", "IDEA.NS",
    "ZOMATO.BO", "PAYTM.NS", "NYKAA.NS"
]

INTERVAL = "5m"
PERIOD = "5d"


# ===============================
# CORE PROCESSING FUNCTION
# ===============================
def process_stock(symbol):

    try:
        df = get_market_data(symbol=symbol, interval=INTERVAL, period=PERIOD)

        if df is None or df.empty:
            return None

        df = create_features(df)
        df = detect_all(df)
        signal = generate_signal(df)

        if signal not in ["BUY", "SELL"]:
            return None

        return (symbol, signal)

    except:
        return None


# ===============================
# MAIN EXECUTION
# ===============================
if __name__ == "__main__":

    results = []

    for stock in WATCHLIST:
        result = process_stock(stock)

        if result:
            results.append(result)

        time.sleep(0.3)

    # ===============================
    # FINAL OUTPUT ONLY (CLEAN)
    # ===============================
    if results:
        for symbol, signal in results:
            print(f"{symbol} → {signal}")
    else:
        print("No BUY/SELL signals found")
