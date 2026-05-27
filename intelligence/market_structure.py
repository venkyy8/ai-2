from indicators.support_resistance import (
    get_support_resistance,
    is_breakout,
    is_breakdown
)

def analyze_structure(df):
    price = df["close"].iloc[-1]

    support, resistance = get_support_resistance(df)

    breakout = is_breakout(price, resistance)
    breakdown = is_breakdown(price, support)

    if breakout:
        return "BREAKOUT_BULLISH", support, resistance

    if breakdown:
        return "BREAKDOWN_BEARISH", support, resistance

    return "RANGE", support, resistance