class Vehicle:  # Base class
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def move(self):
        print(f"{self.brand} moves at {self.speed} km/h")

class GPSMixin:  # Extra ability
    def get_location(self):
        return "GPS: 40.7128° N, 74.0060° W"

class ElectricMixin:  # Extra ability
    def charge(self):
        print(f"{self.brand} is charging...")

class Car(Vehicle, GPSMixin):  # Inherits Vehicle + GPS
    def honk(self):
        print("Car horn: Beep Beep!")

class Bike(Vehicle, ElectricMixin):  # Inherits Vehicle + Electric
    def ring_bell(self):
        print("Bike bell: Ring Ring!")

# Usage
car = Car("Toyota", 120)
bike = Bike("eBike", 40)

car.move()
print(car.get_location())
car.honk()

bike.move()
bike.charge()
bike.ring_bell()
