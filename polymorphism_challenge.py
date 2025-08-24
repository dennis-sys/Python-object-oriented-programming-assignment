# polymorphism_challenge.py

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Bike:
    def move(self):
        print("Cycling 🚲")

# Example usage:
vehicles = [Car(), Plane(), Bike()]

for vehicle in vehicles:
    vehicle.move()  # Each will print its own version!
