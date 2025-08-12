hours = int(input("Enter parking hours: "))
if hours <= 2:
    fee = 50
elif hours <= 5:
    fee = 50 + (hours - 2) * 20
else:
    fee = 110 + (hours - 5) * 30
print(f"Parking fee: ₹{fee}")
