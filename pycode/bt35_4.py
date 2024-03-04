# Duck Typing:

class Car:
    def drive(self):
        print("Car is being driven")

class Plane:
    def drive(self):
        print("Plane is being flown")

def drive_vehicle(vehicle):
    vehicle.drive()

# Polymorphism in action
drive_vehicle(Car())    # Output: Car is being driven
drive_vehicle(Plane())  # Output: Plane is being flown