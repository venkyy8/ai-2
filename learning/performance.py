import json

FILE = "trade_memory.json"

def get_success_rate():

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        if not data:
            return 50

        wins = 0
        total = len(data)

        for t in data:
            if "BUY" in t.get("signal", ""):
                wins += 1  # placeholder logic (upgrade later with exit tracking)

        return (wins / total) * 100

    except:
        return 50