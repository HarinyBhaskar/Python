wishlist = {
    "Alice": ["Shoes", "Bag"],
    "Bob": ["Watch"]
}

# Set of all unique items wished by users
unique_items = set(["Shoes", "Bag", "Watch"])

def add_item(user, item):
    wishlist.setdefault(user, []).append(item)
    unique_items.add(item)
    print(f"{user} added {item} to wishlist.")

def show_wishlist():
    print("\nWishlists:")
    for user, items in wishlist.items():
        print(f"{user}: {items}")

add_item("Alice", "Perfume")
add_item("Charlie", "Shoes")
show_wishlist()
print("Unique items wished:", unique_items)
