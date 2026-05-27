import json

FILE = "trade_memory.json"

def evaluate_trade(symbol, exit_price):

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        for trade in reversed(data):

            if trade["symbol"] == symbol and "outcome" not in trade:

                entry = trade["price"]

                if trade["signal"] == "BUY":
                    trade["outcome"] = "WIN" if exit_price > entry else "LOSS"

                elif trade["signal"] == "SELL":
                    trade["outcome"] = "WIN" if exit_price < entry else "LOSS"

                break

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

    except:
        pass