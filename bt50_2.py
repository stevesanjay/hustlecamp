# Using the pdb Debugger:

import pdb

def divide(x, y):
    pdb.set_trace()  # Set a breakpoint
    result = x / y
    return result

# Example usage with pdb for debugging
numerator = 10
denominator = 0
result = divide(numerator, denominator)