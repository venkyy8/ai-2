import pandas as pd
import os


MEMORY_FILE = "output/trade_memory.csv"


def save_trade(data):
    if os.path.exists(MEMORY_FILE):
        df = pd.read_csv(MEMORY_FILE)
        df = pd.concat([df, pd.DataFrame([data])])
    else:
        df = pd.DataFrame([data])

    df.to_csv(MEMORY_FILE, index=False)