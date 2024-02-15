# Defining a Simple Class:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Toyota", "Camry", 2020)
print(my_car.make, my_car.model, my_car.year)