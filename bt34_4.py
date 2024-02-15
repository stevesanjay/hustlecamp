# Encapsulation with Private Methods:

class TemperatureConverter:
    def __init__(self):
        pass

    def __celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32  # Private method

    def convert_to_fahrenheit(self, celsius):
        return self.__celsius_to_fahrenheit(celsius)


converter = TemperatureConverter()
print("30 Celsius in Fahrenheit:", converter.convert_to_fahrenheit(30))  # Output: 86.0
