# Basic Method Overriding:

class Parent:
    def display(self):
        print("Parent class method")

class Child(Parent):
    def display(self):
        print("Child class method overriding parent method")

# Creating objects
parent_obj = Parent()
child_obj = Child()

# Calling methods
parent_obj.display()  # Output: Parent class method
child_obj.display()   # Output: Child class method overriding parent method