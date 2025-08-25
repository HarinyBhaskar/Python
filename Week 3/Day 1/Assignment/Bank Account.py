class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self.balance += amount
        print(f"Deposited: Rs{amount}, Balance = Rs{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive!")
        if amount > self.balance:
            raise ValueError("Overdraw not allowed!")
        self.balance -= amount
        print(f"Withdrew: Rs{amount}, Balance = Rs{self.balance}")


# ---- User Input Demo ----
owner = input("Enter account owner name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(owner, initial_balance)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        try:
            account.deposit(amt)
        except ValueError as e:
            print("Error:", e)

    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        try:
            account.withdraw(amt)
        except ValueError as e:
            print("Error:", e)

    elif choice == "3":
        print("Exiting. Final Balance:", account.balance)
        break
    else:
        print("Invalid option. Try again!")
