from datetime import datetime

weather_data = {
    "Chennai": "Sunny, 33°C",
    "Delhi": "Cloudy, 29°C",
    "Bangalore": "Rainy, 25°C"
}

city = "Chennai"
print("Weather Report")
print("Date & Time:", datetime.now().strftime("%d-%m-%Y %H:%M"))
print(f"{city}: {weather_data[city]}")
