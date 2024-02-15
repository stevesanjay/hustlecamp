# Importing All Functions from a Module (Not Recommended):

# File: my_module.py
def greet(name):
    print(f"Hello, {name}!")

def farewell(name):
    print(f"Goodbye, {name}!")

# File: main.py
from my_module import *

greet("Alice")
farewell("Bob")