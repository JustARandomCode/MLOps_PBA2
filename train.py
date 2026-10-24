import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

FEATURES = ["age", "tenure_months", "monthly_spend"]


def load_data(path="data/customers.csv"):
    return pd.read_csv(path)


def train(df):
    X_train, X_test, y_train, y_test = train_test_split(
        df[FEATURES], df["churn"], test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test


if __name__ == "__main__":
    model, X_test, y_test = train(load_data())
    print("Accuracy:", model.score(X_test, y_test))