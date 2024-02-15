# Importing Modules with Aliases:

# File: my_module.py
def greet(name):
    print(f"Hello, {name}!")

# File: main.py
import my_module as mm

mm.greet("Alice")