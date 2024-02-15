# Custom Exception with Multiple Arguments:

class InvalidInputError(Exception):
    def __init__(self, input_value, input_type):
        self.input_value = input_value
        self.input_type = input_type

    def __str__(self):
        return f"Invalid input value '{self.input_value}' of type '{self.input_type}'."

def validate_input(input_data):
    if not isinstance(input_data, int):
        raise InvalidInputError(input_data, type(input_data))
    else:
        print("Input is valid.")

try:
    validate_input("abc")
except InvalidInputError as e:
    print("Custom Error:", e)