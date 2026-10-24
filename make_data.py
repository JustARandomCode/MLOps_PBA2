import os
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
n = 500
df = pd.DataFrame({
    "customer_id": range(n),
    "age": rng.integers(18, 70, n),
    "tenure_months": rng.integers(1, 60, n),
    "monthly_spend": rng.uniform(10, 200, n).round(2),
})
df["churn"] = ((df.tenure_months < 24) & (df.monthly_spend > 90)).astype(int)

os.makedirs("data", exist_ok=True)
df.to_csv("data/customers.csv", index=False)