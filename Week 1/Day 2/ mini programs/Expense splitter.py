print("=== Expense Splitter ===")
total_expense = input("Enter total expense: ")
total_expense = float(total_expense)

people = input("Enter number of people: ")
people = int(people)

share = total_expense / people
print("Each person should pay: ₹", round(share, 2))

extra = input("Enter any tip amount (₹): ")
extra = float(extra)
total_with_tip = total_expense + extra
print("With tip, each pays: ₹", round(total_with_tip / people, 2))
