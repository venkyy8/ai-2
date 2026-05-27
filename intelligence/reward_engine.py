def calculate_reward(outcome, confidence):

    if outcome == "WIN":
        return confidence * 1.2   # reward good trades

    if outcome == "LOSS":
        return -confidence        # penalize bad trades

    return 0