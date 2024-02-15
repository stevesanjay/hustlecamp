# Encapsulation with Getter and Setter Methods:

class Car:
    def __init__(self, speed):
        self.__speed = speed  # Encapsulated attribute

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        if new_speed > 0:
            self.__speed = new_speed


car = Car(100)
print("Current speed:", car.get_speed())  # Output: 100
car.set_speed(120)
print("Updated speed:", car.get_speed())  # Output: 120
