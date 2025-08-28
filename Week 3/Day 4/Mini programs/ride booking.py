import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def book_ride(user, destination):
    return f"✅ Ride booked for {user} to {destination}"

user = input("Enter passenger name: ")
dest = input("Enter destination: ")
print(book_ride(user, dest))
