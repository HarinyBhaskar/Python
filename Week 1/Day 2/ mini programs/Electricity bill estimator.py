distance = input("Enter trip distance in km: ")
distance = float(distance)
mileage = input("Enter vehicle mileage (km/l): ")
mileage = float(mileage)
price_per_liter = input("Enter fuel price per liter: ")
price_per_liter = float(price_per_liter)
liters_needed = distance / mileage
total_cost = liters_needed * price_per_liter
print("Fuel required:", liters_needed, "liters")
print("Trip cost: ₹", total_cost)
