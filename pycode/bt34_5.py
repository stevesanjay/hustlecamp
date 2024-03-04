# Encapsulation with Private Attributes:

class Product:
    def __init__(self, name, price):
        self.__name = name  # Encapsulated attribute
        self.__price = price  # Encapsulated attribute

    def display_info(self):
        print(f"Product: {self.__name}, Price: ${self.__price}")


product = Product("Laptop", 999)
product.display_info()  # Output: Product: Laptop, Price: $999
# Attempting to access private attributes directly will result in an AttributeError
# print(product.__name)  
# print(product.__price)