# Custom Exception with Error Message:

class ValueTooLargeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value {self.value} is too large."

def process_value(x):
    max_value = 100
    if x > max_value:
        raise ValueTooLargeError(x)
    else:
        print("Value is within acceptable range.")

try:
    process_value(150)
except ValueTooLargeError as e:
    print("Custom Error:", e)