import logging
logging.basicConfig(filename="bank.log", level=logging.INFO)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance
        logging.info("Created account for %s with %s", owner, balance)

    def deposit(self, amount):
        if amount <= 0:
            logging.error("Invalid deposit: %s", amount)
            raise ValueError("Deposit must be positive")
        self.balance += amount
        logging.info("Deposited %s, new balance %s", amount, self.balance)
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            logging.error("Overdraft attempt %s by %s", amount, self.owner)
            raise ValueError("Insufficient funds")
        self.balance -= amount
        logging.info("Withdrew %s, new balance %s", amount, self.balance)
        return self.balance

if __name__ == "__main__":
    acc = BankAccount(input("Enter name: "), float(input("Initial balance: ")))
    acc.deposit(float(input("Deposit amount: ")))
    try:
        print("Final balance:", acc.withdraw(float(input("Withdraw amount: "))))
    except ValueError as e:
        print("Error:", e)
