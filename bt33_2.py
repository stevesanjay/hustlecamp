# Accessing Parent Class Method in Child Class:

class Parent:
    def display(self):
        print("Parent class method")

class Child(Parent):
    def display(self):
        super().display()  # Calling parent class method
        print("Child class method")

# Creating object
child_obj = Child()

# Calling method
child_obj.display()
# Output:
# Parent class method
# Child class method