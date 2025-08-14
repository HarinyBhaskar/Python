# Grocery Billing & Stock Tracker

inventory = [
    ("Apples", 50, 0.5),
    ("Bananas", 30, 0.3),
    ("Milk", 20, 1.5),
    ("Bread", 15, 2.0)
]

def display_inventory():
    print("\nCurrent Inventory:")
    for item, qty, price in inventory:
        print(f"{item}: {qty} units - ${price:.2f} each")

def update_stock(item_name, sold_qty):
    for i, (item, qty, price) in enumerate(inventory):
        if item.lower() == item_name.lower():
            if sold_qty <= qty:
                inventory[i] = (item, qty - sold_qty, price)
                print(f"Sold {sold_qty} {item}(s). Stock left: {qty - sold_qty}")
            else:
                print(f"Not enough stock for {item}")
            return
    print("Item not found.")

def calculate_total(order):
    return sum(qty * price for name, qty, price in order)

# Simulation
display_inventory()
order = [("Apples", 5, 0.5), ("Milk", 2, 1.5)]
for item, qty, price in order:
    update_stock(item, qty)

display_inventory()
total = calculate_total(order)
print(f"\nTotal Bill: ${total:.2f}")
