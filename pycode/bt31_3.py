# Updating Instance Variable:

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Corolla")
car1.model = "Camry"
print(car1.model)  # Output: Camry