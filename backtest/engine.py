
def backtest(df, signals):
    balance = 10000
    position = 0

    for i in range(len(signals)):
        price = df.iloc[i]["close"]

        if signals[i] == 1:  # BUY
            position = price

        elif signals[i] == 0 and position != 0:  # SELL
            balance += price - position
            position = 0

    return balance
