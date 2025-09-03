import numpy as np
import pandas as pd

# Fake sales dataset
data = {
    "Product": ["Shoes", "Shoes", "Bags", "Bags", "Watch", "Watch"],
    "Month": ["Jan", "Feb", "Jan", "Feb", "Jan", "Feb"],
    "Sales": [200, 250, 300, 350, 400, 450]
}

df = pd.DataFrame(data)

# NumPy for growth calculation
sales = df["Sales"].to_numpy()
growth = np.diff(sales)   # difference between months

df["Growth"] = np.append([np.nan], growth)  # align sizes
print(df)

# Avg sales by product
print("\nAverage sales per product:")
print(df.groupby("Product")["Sales"].mean())
