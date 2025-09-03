import numpy as np
import pandas as pd

# Fake stock prices
prices = {
    "Day": pd.date_range(start="2024-01-01", periods=6),
    "Price": [100, 102, 105, 103, 108, 110]
}
df = pd.DataFrame(prices)

# Daily returns (NumPy diff)
df["Return"] = np.append([np.nan], np.diff(df["Price"]) / df["Price"][:-1])

# Moving average (3-day)
df["Moving_Avg"] = df["Price"].rolling(3).mean()

print(df)
