# Instance Variable Example:

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.make)   # Output: Toyota
print(car1.model)  # Output: Corolla