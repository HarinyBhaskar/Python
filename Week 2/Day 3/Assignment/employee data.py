import csv
import json
import os

# -------------------------------
# Program: Convert CSV → JSON
# Data: Employee records
# -------------------------------

# Input CSV filename
csv_file = r"C:\Users\harin\OneDrive\Desktop\python\week 2\Day 3\data.csv"

# Output JSON filename
json_file = "employees.json"

# Check if CSV file exists
if not os.path.exists(csv_file):
    print(f"Error: {csv_file} not found! Please create the file first.")
    exit()

# List to store employee records
employees = []

# Step 1: Read CSV file
with open(csv_file, mode="r", newline="") as f:
    reader = csv.DictReader(f)  # Reads rows as dictionaries
    for row in reader:
        # Convert values properly
        employee = {
            "name": row["name"].title(),   # Capitalize first letter
            "age": int(row["age"]),        # Convert age to integer
            "dept": row["dept"].capitalize()  # Capitalize department
        }
        employees.append(employee)

# Step 2: Print employees list (for debugging)
print("Employee Records:")
for emp in employees:
    print(emp)

# Step 3: Write JSON output to file
with open(json_file, "w") as f:
    json.dump(employees, f, indent=4)

print(f"\n Successfully converted {csv_file} → {json_file}")
