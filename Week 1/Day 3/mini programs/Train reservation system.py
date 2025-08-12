print(" Indian Railways  ")
classes = {"Sleeper": 150, "AC": 400 "First class":700}

for cls, price in classes.items():
    print(f"{cls} - Rs{price} per ticket")
    
cls_choice = input("Enter class of ticket: ").title()

if cls_choice in classes:
    tickets = int(input("enter the number of tickets:"))
    bill = tickets * classes[cls_choice]

    food = input("Do you want meals included? (yes/no): ").lower()
    if food == "yes":
        bill += tickets * 100

    age = int(input("Enter passenger age: "))
    if age < 12:
        bill *= 0.5
    elif age >= 60:
        bill *= 0.7

    print(f"Class: {cls_choice}")
    print(f"Tickets: {tickets}")
    print(f"Total Price: ₹{bill}")
else:
    print("Invalid class choice.")