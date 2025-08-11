print(" Holiday Budget Planner ")
budget = input("Enter your total holiday budget: ₹ ")
budget = float(budget)

accommodation = budget * 0.4   # 40% for hotel
food = budget * 0.3            # 30% for food
activities = budget * 0.2      # 20% for activities
misc = budget * 0.1            # 10% for other expenses

print("Accommodation: ₹", round(accommodation, 2))
print("Food: ₹", round(food, 2))
print("Activities: ₹", round(activities, 2))
print("Miscellaneous: ₹", round(misc, 2))
