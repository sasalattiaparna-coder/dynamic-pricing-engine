from sklearn.model_selection import train_test_split 
from xgboost import XGBRegressor 
import joblib 
from data import generate_data

def train():
    df = generate_data()

    X = df[["demand", "inventory", "competitor_price", "season"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBRegressor(n_estimators=300, learning_rate=0.05)
    model.fit(X_train, y_train)

    joblib.dump(model, "model.pkl")
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train()