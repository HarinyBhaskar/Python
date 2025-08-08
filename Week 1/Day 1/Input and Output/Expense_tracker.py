total = 0
entries = int(input("How many expenses? "))
for _ in range(entries):
    item = input("Expense name: ")
    cost = float(input("Cost: "))
    total += cost
    print(f"Added {item} - ${cost:.2f}")
print(f"Total expenses: ${total:.2f}")
