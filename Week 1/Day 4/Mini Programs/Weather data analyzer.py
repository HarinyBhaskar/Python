print(" Weather Data Analyzer ")
days = int(input("Enter number of days to record: "))

temperatures = []

for day in range(1, days + 1):
    temp = float(input(f"Enter temperature for Day {day}: "))
    temperatures.append(temp)

while True:
    print("\n Menu ")
    print("1. Show all temperatures")
    print("2. Show highest temperature")
    print("3. Show lowest temperature")
    print("4. Show average temperature")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Temperatures:", temperatures)
    elif choice == "2":
        print("Highest temperature:", max(temperatures))
    elif choice == "3":
        print("Lowest temperature:", min(temperatures))
    elif choice == "4":
        avg_temp = sum(temperatures) / len(temperatures)
        print("Average temperature:", round(avg_temp, 2))
    elif choice == "5":
        print("Exiting Weather Analyzer. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
