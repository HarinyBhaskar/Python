balance = 5000
pin = "1234"

print(" welcome to abc bank")
entered_pin = input("enter your 4 digit pin: ")

if entered_pin != pin:
    print("Incorrect pin. Transaction cancelled.")
else:
    amount = int(input("enter amount to withdraw:"))  
     
     if amount <= 0:
       print("invalid amount")

    elif amount > balance:
        print("Insufficient balance. Transaction cancelled.")
    
    else:
    balance -= amount
    print(f"withdrawal successful!! You withdrew Rs{amount}.")
    print(f" remaining balance: Rs{balance}")
