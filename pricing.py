import joblib 

model = joblib.load("model.pkl")

def dynamic_price(demand, inventory, competitor_price, season):
    base = model.predict([[demand, inventory, competitor_price, season]])[0]

    # Business logic
    if demand > 80:
        base *= 1.2

    if inventory < 20:
        base *= 1.1

    if competitor_price < base:
        base = competitor_price - 3

    return round(base, 2)