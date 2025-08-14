# Airport Flight Schedule
flights = [
    ("AA101", "New York", "10:30"),
    ("BA202", "London", "14:15"),
    ("CA303", "Tokyo", "18:45")
]

def display_flights():
    print("\nToday's Flights:")
    for code, destination, time in flights:
        print(f"Flight {code} to {destination} departs at {time}")

def add_flight(code, dest, time):
    flights.append((code, dest, time))
    print(f"Flight {code} added.")

display_flights()
add_flight("DA404", "Dubai", "22:00")
display_flights()
