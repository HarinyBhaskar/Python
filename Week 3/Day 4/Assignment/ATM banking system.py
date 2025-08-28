import time
import logging
from functools import wraps

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Timed decorator
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper


# --- Real-World ATM Functions ---
@timed
def check_balance(user):
    time.sleep(1)  # simulate database call
    return f"Balance for {user['name']}: ₹{user['balance']}"

@timed
def withdraw_money(user, amount):
    time.sleep(2)  # simulate transaction processing
    if amount > user['balance']:
        return "Insufficient funds"
    user['balance'] -= amount
    return f"Withdrawal of ₹{amount} successful. New balance: ₹{user['balance']}"

@timed
def deposit_money(user, amount):
    time.sleep(1.5)  # simulate transaction processing
    user['balance'] += amount
    return f"Deposit of ₹{amount} successful. New balance: ₹{user['balance']}"


# --- Main Program ---
if __name__ == "__main__":
    user = {"name": input("Enter your name: "), "balance": 5000}

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(check_balance(user))
        elif choice == "2":
            amt = int(input("Enter amount to withdraw: "))
            print(withdraw_money(user, amt))
        elif choice == "3":
            amt = int(input("Enter amount to deposit: "))
            print(deposit_money(user, amt))
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice, try again.")
