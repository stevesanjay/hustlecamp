# Importing Specific Functions from a Module:

# File: my_module.py
def greet(name):
    print(f"Hello, {name}!")

def farewell(name):
    print(f"Goodbye, {name}!")

# File: main.py
from my_module import greet

greet("Alice")