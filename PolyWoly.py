# Base class
class Vehicle:
    def move(self):
        pass  # Placeholder for subclass implementations

# Subclasses with different behaviors
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚢"

class Horse(Vehicle):  # Bonus: an animal as a vehicle in old times!
    def move(self):
        return "Galloping on the ground 🐎"

# Polymorphism in action
def describe_movement(vehicle):
    print(vehicle.move())

# Create a list of vehicle instances
vehicles = [Car(), Plane(), Boat(), Horse()]

# Loop through each and show how they move
for v in vehicles:
    describe_movement(v)
