# Logging:

import logging

logging.basicConfig(level=logging.DEBUG)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logging.error("Error occurred: %s", e, exc_info=True)
        result = None
    return result

# Example usage with logging for debugging
numerator = 10
denominator = 0
result = divide(numerator, denominator)