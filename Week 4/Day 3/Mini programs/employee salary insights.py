import numpy as np
import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D", "E"],
    "Salary": [4000, 5000, 6000, 7000, 8000]
}
df = pd.DataFrame(data)

# Bonus = 10% of salary using NumPy
df["Bonus"] = np.multiply(df["Salary"], 0.10)

# Salary statistics
print("Salary Mean:", np.mean(df["Salary"]))
print("Salary Std Dev:", np.std(df["Salary"]))
print("\nEmployee Data:\n", df)
