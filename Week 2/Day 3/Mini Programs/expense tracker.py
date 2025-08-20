import csv, datetime, os

base_path = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(base_path, "expenses.csv")
summary_file = os.path.join(base_path, "summary.txt")

# Ensure CSV has headings
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Item", "Amount", "Date"])

# Add expense
item = input("Enter expense item: ")
amount = float(input("Enter amount: "))

with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([item, amount, datetime.datetime.now().strftime("%Y-%m-%d")])

# Calculate total so far
total = 0
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += float(row["Amount"])

# Write summary in TXT
with open(summary_file, "a") as f:
    f.write(f"{datetime.datetime.now()} - Added {item} ({amount}). Total so far = {total}\n")

print(" Expense added in expenses.csv and summary updated in summary.txt")
