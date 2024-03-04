# Simple Custom Exception:

class CustomError(Exception):
    pass

def example_function(x):
    if x < 0:
        raise CustomError("Input should be a non-negative number.")
    else:
        print("Input is valid.")

try:
    example_function(-5)
except CustomError as e:
    print("Custom Error:", e)
