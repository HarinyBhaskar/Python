class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance: {self.balance}")
        else:
            print("❌ Insufficient funds")

# --- Mixins ---
class SMSAlertMixin:
    def send_alert(self, msg):
        print(f"📩 SMS to {self.owner}: {msg}")

class TransactionHistoryMixin:
    def __init__(self):
        self.history = []
    def log(self, action):
        self.history.append(action)

# --- Inheritance + Mixins ---
class SavingsAccount(BankAccount, SMSAlertMixin, TransactionHistoryMixin):
    def __init__(self, owner, balance=0, rate=0.03):
        BankAccount.__init__(self, owner, balance)
        TransactionHistoryMixin.__init__(self)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.balance += interest
        self.log(f"Interest added: {interest}")
        self.send_alert(f"Interest credited: {interest}")
        return interest

# --- Program with User Input ---
name = input("Enter account holder name: ")
acc = SavingsAccount(name, float(input("Enter initial deposit: ")), 0.05)

while True:
    print("\n1.Deposit  2.Withdraw  3.Add Interest  4.History  5.Exit")
    choice = input("Choose option: ")
    
    if choice == "1":
        amt = float(input("Enter deposit amount: "))
        acc.deposit(amt)
        acc.log(f"Deposited {amt}")
    elif choice == "2":
        amt = float(input("Enter withdrawal amount: "))
        acc.withdraw(amt)
        acc.log(f"Withdrew {amt}")
    elif choice == "3":
        acc.add_interest()
    elif choice == "4":
        print("Transaction history:", acc.history)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print(" Invalid choice")
