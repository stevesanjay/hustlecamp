# Inheritance:

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

my_dog = Dog()
my_cat = Cat()
print(my_dog.speak())
print(my_cat.speak())