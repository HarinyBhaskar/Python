import numpy as np
import pandas as pd

data = {
    "Day": pd.date_range(start="2024-01-01", periods=7),
    "Temperature": [30, np.nan, 32, 31, np.nan, 29, 28]
}
df = pd.DataFrame(data)

# Fill missing with mean temperature (NumPy + pandas)
mean_temp = np.nanmean(df["Temperature"].to_numpy())
df["Temperature"].fillna(mean_temp, inplace=True)

print(df)
