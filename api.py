from fastapi import FastAPI 
from pricing import dynamic_price

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Dynamic Pricing Engine Running"}

@app.get("/predict")
def predict(demand: int, inventory: int, competitor_price: float, season: int):
    price = dynamic_price(demand, inventory, competitor_price, season)
    return {"dynamic_price": price}