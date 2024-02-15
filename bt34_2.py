# Encapsulation with Property Decorators:

class Person:
    def __init__(self, name):
        self.__name = name  # Encapsulated attribute

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


person = Person("John")
print(person.name)  # Output: John
person.name = "Alice"
print(person.name)  # Output: Alice