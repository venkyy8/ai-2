import json
import os
from datetime import datetime

FILE = "trade_memory.json"


def _load_data():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def _save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def save_trade(trade):
    """
    Save new trade entry (entry time snapshot)
    """

    data = _load_data()

    trade["time"] = str(datetime.now())
    trade["outcome"] = None   # will be updated later

    data.append(trade)

    _save_data(data)


def update_trade_outcome(symbol, exit_price):
    """
    Mark WIN / LOSS after trade completion
    """

    data = _load_data()

    for trade in reversed(data):

        if trade["symbol"] == symbol and trade["outcome"] is None:

            entry = trade["price"]

            if trade["signal"] == "BUY":
                trade["outcome"] = "WIN" if exit_price > entry else "LOSS"

            elif trade["signal"] == "SELL":
                trade["outcome"] = "WIN" if exit_price < entry else "LOSS"

            break

    _save_data(data)


def get_success_rate():
    """
    Simple learning metric
    """

    data = _load_data()

    if not data:
        return 50

    wins = 0
    total = 0

    for t in data:
        if t.get("outcome") is not None:
            total += 1
            if t["outcome"] == "WIN":
                wins += 1

    if total == 0:
        return 50

    return (wins / total) * 100