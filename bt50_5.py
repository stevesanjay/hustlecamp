# Using Assertion:

def divide(x, y):
    assert y != 0, "Denominator cannot be zero"
    result = x / y
    return result

# Example usage with assertion for debugging
numerator = 10
denominator = 0
result = divide(numerator, denominator)