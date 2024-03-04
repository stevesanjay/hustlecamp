# Accessing Parent Class Methods:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        super().speak()  # Call the parent class method
        print("Dog barks")

dog = Dog()
dog.bark()   # Output: Animal speaks \n Dog barks