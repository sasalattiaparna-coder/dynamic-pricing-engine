import pandas as pd 
import numpy as np 

def generate_data(n=2000):
    np.random.seed(42)

    df = pd.DataFrame({
        "demand": np.random.randint(10, 100, n),
        "inventory": np.random.randint(5, 200, n),
        "competitor_price": np.random.uniform(50, 500, n),
        "season": np.random.choice([0, 1], n)
    })

    df["price"] = (
        0.6 * df["competitor_price"]
        + 0.25 * df["demand"]
        - 0.15 * df["inventory"]
        + 25 * df["season"]
    )

    return df