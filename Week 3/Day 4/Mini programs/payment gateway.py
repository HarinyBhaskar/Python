import time, logging
from functools import wraps
import random

logging.basicConfig(level=logging.INFO)

def retry(retries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.warning(f"Attempt {attempt+1} failed: {e}")
                    time.sleep(1)
            raise Exception("❌ Payment Failed")
        return wrapper
    return decorator

@retry(retries=3)
def process_payment(amount):
    if random.choice([True, False]):
        raise ValueError("Network error")
    return f"✅ Payment of ₹{amount} successful"

amount = float(input("Enter payment amount: "))
print(process_payment(amount))
