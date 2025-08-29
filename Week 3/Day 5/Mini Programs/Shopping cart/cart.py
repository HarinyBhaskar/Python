# cart.py
import logging
logging.basicConfig(filename="cart.log", level=logging.INFO)

class Cart:
    def __init__(self):
        self.items = {}
        logging.info("New cart created")

    def add_item(self, name, price):
        if price <= 0:
            logging.error("Bad price %s", price)
            raise ValueError("Price must be > 0")
        self.items[name] = self.items.get(name, 0) + price
        logging.info("Added %s: %s", name, price)

    def total(self):
        tot = sum(self.items.values())
        logging.info("Cart total %s", tot)
        return tot

if __name__ == "__main__":
    c = Cart()
    for _ in range(int(input("How many items? "))):
        nm, pr = input("Name price: ").split()
        c.add_item(nm, float(pr))
    print("Cart total:", c.total())
