# Function Polymorphism with Multiple Arguments:

def multiply(a, b=None):
    if b is None:
        return a * a  # Square if only one argument is passed
    else:
        return a * b  # Multiply if two arguments are passed

print(multiply(5))     # Output: 25
print(multiply(5, 3))  # Output: 15