filename = "weather_log.txt"
day = input("Enter date (YYYY-MM-DD): ")
temp = input("Enter temperature in °C: ")

with open(filename, "a") as f:
    f.write(f"{day}: {temp}°C\n")

print("Weather data saved.")
