# Modifying Class Variable:

class Car:
    wheels = 4  # Class variable
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Modifying class variable
Car.wheels = 6

car1 = Car("Toyota", "Corolla")
print(car1.wheels)  # Output: 6