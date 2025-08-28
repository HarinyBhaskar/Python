import time, logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def rate_limit(limit, interval):
    calls = []
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            while calls and now - calls[0] > interval:
                calls.pop(0)
            if len(calls) >= limit:
                logging.warning("Too many cart updates!")
                return None
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(limit=3, interval=5)
def add_to_cart(item):
    logging.info(f"Item {item} added to cart")

for i in range(5):
    add_to_cart(f"Product-{i}")
    time.sleep(1)
