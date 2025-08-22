from collections import Counter

orders = ["Pizza", "Burger", "Pizza", "Pasta", "Burger", "Pizza"]

menu = {"Pizza": 200, "Burger": 120, "Pasta": 150}

order_count = Counter(orders)

print("Order Summary:\n")
total = 0
for item, qty in order_count.items():
    price = menu[item] * qty
    total += price
    print(f"{item} x {qty} = Rs.{price}")

print("\nTotal Bill = Rs.", total)
