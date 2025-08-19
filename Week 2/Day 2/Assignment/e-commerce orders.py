# --- Custom map & filter ---
def my_map(func, iterable):
    return [func(item) for item in iterable]

def my_filter(func, iterable):
    return [item for item in iterable if func(item)]


# --- Order Registration ---
def create_order(customer, *items, **details):
    return {
        "customer": customer,
        "items": items,           # variable list of items
        "details": details        # flexible details (price, city, discount)
    }


# --- Sample Orders ---
orders = [
    create_order("Ravi", "Shoes", "Bag", price=2500, city="Delhi", discount=200),
    create_order("Sneha", "Laptop", price=45000, city="Mumbai"),
    create_order("Kiran", "Book", "Pen", price=500, city="Chennai", discount=50),
    create_order("Anita", "Watch", price=3000, city="Delhi"),
]

# --- Use my_map & my_filter ---
delhi_orders = my_filter(lambda o: o["details"]["city"] == "Delhi", orders)
totals = my_map(lambda o: o["details"]["price"] - o["details"].get("discount", 0), orders)

print("Orders from Delhi:", [o["customer"] for o in delhi_orders])
print("Final Bill Amounts:", totals)
