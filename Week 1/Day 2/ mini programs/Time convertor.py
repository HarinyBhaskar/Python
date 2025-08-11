minutes = input("Enter total minutes: ")
minutes = int(minutes)
hours = minutes // 60
remaining = minutes % 60
print("Total minutes entered:", minutes)
print("This is equal to", hours, "hours")
print("And", remaining, "minutes")
