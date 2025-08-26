class User:
    def __init__(self, name):
        self.name = name

class DiscountMixin:
    def discount(self, price):
        return price * 0.9

class ReviewMixin:
    def review(self, text):
        print(f"{self.name} reviewed: {text}")

class Customer(User, DiscountMixin, ReviewMixin):
    def buy(self, item, price):
        final = self.discount(price)
        print(f"{self.name} bought {item} for ${final}")

# Usage
c = Customer("John")
c.buy("Laptop", 1000)
c.review("Excellent product!")
