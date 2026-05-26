
from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    features = ["returns","sma_5","sma_10","trend"]

    df = df.copy()
    df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)
    df.dropna(inplace=True)

    X = df[features]
    y = df["target"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model
