import logging
logging.basicConfig(filename="decorator.log", level=logging.INFO)

def log_calls(func):
    def wrapper(*args, **kwargs):
        logging.info("Calling %s with %s %s", func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        logging.info("Result of %s: %s", func.__name__, result)
        return result
    return wrapper

@log_calls
def multiply(a, b):
    return a * b

if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Multiplication result:", multiply(x, y))
