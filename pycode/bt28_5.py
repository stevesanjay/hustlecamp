# Hierarchical Custom Exceptions:

class CustomError(Exception):
    pass

class InputError(CustomError):
    pass

class ValueError(InputError):
    pass

def process_value(x):
    if x < 0:
        raise ValueError("Input should be a non-negative number.")
    else:
        print("Input is valid.")

try:
    process_value(-5)
except ValueError as e:
    print("Value Error:", e)
except InputError as e:
    print("Input Error:", e)
except CustomError as e:
    print("Custom Error:", e)