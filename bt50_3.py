# Using try and except Blocks:


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print("Error:", e)
        result = None
    return result

# Example usage with try-except for debugging
numerator = 10
denominator = 0
result = divide(numerator, denominator)