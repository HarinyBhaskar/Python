store = {
    "Rice": 50,
    "Wheat": 40,
    "Sugar": 30,
    "Oil": 120
}

cart = {}

out_of_stock = {"Sugar"}

def add_to_cart(item, qty):
    if item in out_of_stock:
        print(f"Sorry, {item} is out of stock.")
    elif item in store:
        cart[item] = cart.get(item, 0) + qty
        print(f"Added {qty} {item}(s) to cart.")

def checkout():
    total = 0
    print("\nCart Summary:")
    for item, qty in cart.items():
        cost = store[item] * qty
        total += cost
        print(f"{item} x{qty} = ₹{cost}")
    print("Total Bill = ₹", total)

add_to_cart("Rice", 2)
add_to_cart("Sugar", 1)
add_to_cart("Oil", 1)
checkout()
