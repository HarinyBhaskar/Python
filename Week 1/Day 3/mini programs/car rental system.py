# Car Rental System

cars = {
    1: {"type": "Sedan", "rate": 2000},
    2: {"type": "SUV", "rate": 3000},
    3: {"type": "Hatchback", "rate": 1500}
}

print("Available Cars for Rent:")
for key, car in cars.items():
    print(f"{key}. {car['type']} - Rs.{car['rate']} per day")

choice = int(input("Choose car (1-3): "))
if choice not in cars:
    print("Invalid choice!")
else:
    days = int(input("Enter number of days: "))
    total = cars[choice]["rate"] * days
    
    driver_needed = input("Need driver? (yes/no): ").lower()
    if driver_needed == "yes":
        total += 1000 * days  # Driver cost per day
    
    print(f"You booked {cars[choice]['type']} for {days} days.")
    print(f"Total cost: Rs.{total}")
