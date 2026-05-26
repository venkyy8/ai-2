def backtest(data, strategy_func):
    wins = 0
    losses = 0

    for i in range(50, len(data)):
        signal = strategy_func(data[:i])

        if signal == "BUY":
            entry = data.iloc[i]["Close"]
            exit_ = data.iloc[i+1]["Close"]

            if exit_ > entry:
                wins += 1
            else:
                losses += 1

    total = wins + losses

    if total == 0:
        return 0

    return (wins / total) * 100
