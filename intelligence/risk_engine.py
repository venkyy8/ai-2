def calculate_levels(price):
    stop_loss = round(price * 0.98, 2)
    target = round(price * 1.04, 2)

    return stop_loss, target