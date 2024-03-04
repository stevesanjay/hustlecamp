# Creating and Importing a Package:

# Copy code
# my_package/
#     __init__.py
    # module1.py
    # module2.py


# File: my_package/module1.py
def func1():
    print("Function 1")

# File: my_package/module2.py
def func2():
    print("Function 2")

# File: main.py
from my_package import module1, module2

module1.func1()
module2.func2()