import logging

logging.basicConfig(filename="shop.log", level=logging.INFO)

cart = {"Laptop": 60000, "Phone": 30000}

try:
    item = input("Enter item to buy: ")
    if item not in cart:
        raise KeyError("Item not found")
    qty = int(input("Enter quantity: "))
    if qty <= 0:
        raise ValueError("Quantity must be positive")
    total = cart[item] * qty
    logging.info(f"Order placed: {item} x {qty} = Rs.{total}")
    print("Order confirmed. Total =", total)
except (KeyError, ValueError) as e:
    logging.error(e)
    print("Error:", e)
