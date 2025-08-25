class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Room {self.number} booked for ${self.price}")
        else:
            print(f"Room {self.number} is already booked!")

    def checkout(self):
        if self.is_booked:
            self.is_booked = False
            print(f"Room {self.number} is now available.")
        else:
            print("Room is already free.")

# Example usage
r1 = Room(101, 100)
r2 = Room(102, 150)

r1.book()
r1.book()
r1.checkout()
