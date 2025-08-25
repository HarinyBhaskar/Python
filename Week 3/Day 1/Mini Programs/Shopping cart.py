class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def total_price(self):
        return sum(p.price for p in self.items)

    def show_cart(self):
        print("Your Cart:")
        for p in self.items:
            print("-", p)
        print(f"Total: ${self.total_price()}")


# Example usage
p1 = Product("Laptop", 1000)
p2 = Product("Mouse", 50)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
cart.show_cart()
