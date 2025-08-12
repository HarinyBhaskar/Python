print(" Electricity Bill ")
units = int(input("Enter units consumed: "))
customer = input("Enter customer type (domestic/commercial): ").lower()

if customer == "domestic":
    if units <= 100:
        rate = 5
    elif units <= 300:
        rate = 8
    else:
        rate = 10
elif customer == "commercial":
    if units <= 100:
        rate = 8
    elif units <= 300:
        rate = 10
    else:
        rate = 15
else:
    print("Invalid customer type.")
    exit()

bill = units * rate

if bill > 2000:
    bill += bill * 0.05  # 5% surcharge

print(f"Units: {units}")
print(f"Rate: ₹{rate}")
print(f"Total Bill: ₹{bill}")
