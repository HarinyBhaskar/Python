choice = input("Convert to (C)elsius or (F)ahrenheit? ").strip().lower()
temp = float(input("Enter the temperature: "))

if choice == "c":
    result = (temp - 32) * 5 / 9
    print(f"{temp}°F is {result:.2f}°C")
elif choice == "f":
    result = (temp * 9 / 5) + 32
    print(f"{temp}°C is {result:.2f}°F")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
