import logging
from functools import wraps, lru_cache

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} called with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class TicketBooking:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked = 0

    @log_action
    def book(self, qty):
        if self.booked + qty <= self.total_seats:
            self.booked += qty
            return f"Booked {qty} seat(s)."
        return "Not enough seats available."

    @lru_cache(maxsize=3)
    def status(self):
        return f"Seats booked: {self.booked}/{self.total_seats}"

if __name__ == "__main__":
    tb = TicketBooking(5)
    while True:
        choice = input("\n1.Book Ticket\n2.Check Status\n3.Exit\nChoice: ")
        if choice == "1":
            qty = int(input("Enter seats to book: "))
            print(tb.book(qty))
        elif choice == "2":
            print(tb.status())
        else:
            break
