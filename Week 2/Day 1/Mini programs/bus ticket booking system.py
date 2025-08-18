buses = {
    "Bus1": 5,
    "Bus2": 3,
    "Bus3": 4
}

# Set of booked buses
booked_buses = set()

def show_buses():
    print("\nAvailable Buses:")
    for bus, seats in buses.items():
        print(f"{bus} - {seats} seats")

def book_ticket(bus_name):
    if bus_name in buses and buses[bus_name] > 0:
        buses[bus_name] -= 1
        booked_buses.add(bus_name)
        print(f"Ticket booked in {bus_name}")
    else:
        print("No seats available!")

show_buses()
book_ticket("Bus1")
book_ticket("Bus1")
print("\nBooked Buses:", booked_buses)
show_buses()
