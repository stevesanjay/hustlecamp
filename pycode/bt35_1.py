# Method Overriding:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_animal_speak(animal):
    animal.speak()

# Polymorphism in action
make_animal_speak(Animal())  # Output: Animal speaks
make_animal_speak(Dog())     # Output: Dog barks
make_animal_speak(Cat())     # Output: Cat meows