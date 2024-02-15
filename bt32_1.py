# Simple Single Inheritance:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks