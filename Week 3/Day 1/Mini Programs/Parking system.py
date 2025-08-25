class Car:
    def __init__(self, plate):
        self.plate = plate

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parked_cars = []

    def park(self, car):
        if len(self.parked_cars) < self.capacity:
            self.parked_cars.append(car)
            print(f"Car {car.plate} parked.")
        else:
            print("Parking Lot Full!")

    def leave(self, car):
        if car in self.parked_cars:
            self.parked_cars.remove(car)
            print(f"Car {car.plate} left the parking lot.")
        else:
            print("Car not found.")

# Example usage
lot = ParkingLot(2)
c1 = Car("KA-01")
c2 = Car("KA-02")
c3 = Car("KA-03")

lot.park(c1)
lot.park(c2)
lot.park(c3)
lot.leave(c1)
