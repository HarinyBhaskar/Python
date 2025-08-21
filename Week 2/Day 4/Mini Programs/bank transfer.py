import logging

logging.basicConfig(filename="transfer.log", level=logging.INFO)

accounts = {"Alice": 5000, "Bob": 3000}

try:
    sender = input("Sender: ")
    receiver = input("Receiver: ")
    amount = int(input("Amount: "))
    if sender not in accounts or receiver not in accounts:
        raise KeyError("Account not found")
    if accounts[sender] < amount:
        raise ValueError("Insufficient balance")
    accounts[sender] -= amount
    accounts[receiver] += amount
    logging.info(f"Transfer: {sender} -> {receiver}, Rs.{amount}")
    print("Transfer successful.")
except (KeyError, ValueError) as e:
    logging.error(e)
    print("Error:", e)
