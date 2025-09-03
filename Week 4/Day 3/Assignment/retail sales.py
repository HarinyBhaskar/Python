import pandas as pd

# Step 1: Load CSV file
df = pd.read_csv("retail_sales.csv")

print("Original Data:")
print(df.head())

# Step 2: Group by Region & ProductCategory
summary = df.groupby(["Region", "ProductCategory"]).agg({
    "Sales": ["sum", "mean", "max"],
    "Profit": ["sum", "mean"]
})

# Step 3: Export the summary to a new CSV
summary.to_csv("retail_sales_summary.csv")

print("\nSummary saved as 'retail_sales_summary.csv'")
print(summary)
