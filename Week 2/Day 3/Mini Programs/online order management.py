import csv, datetime, os

base_path = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(base_path, "orders.csv")
log_file = os.path.join(base_path, "orders_log.txt")

# Ensure CSV has headings
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["OrderID", "Customer", "Item", "Price", "Date"])

# Add order
order_id = input("Enter Order ID: ")
customer = input("Enter Customer Name: ")
item = input("Enter Item: ")
price = float(input("Enter Price: "))

with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([order_id, customer, item, price, datetime.datetime.now().strftime("%Y-%m-%d")])

# Log action
with open(log_file, "a") as f:
    f.write(f"{datetime.datetime.now()} - New Order {order_id} for {customer}, Item: {item}, Price: {price}\n")

print(" Order saved in orders.csv and action logged in orders_log.txt")
