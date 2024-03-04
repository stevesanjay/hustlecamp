# Accessing Class Variable from Instance:

class Car:
    wheels = 4  # Class variable
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.wheels)  # Output: 4