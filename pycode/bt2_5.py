# Docstring for a class:



class Person:
    """
    A class to represent a person.
    """

    def __init__(self, name, age):
        """
        Constructor to initialize the person object.
        :param name: The name of the person
        :param age: The age of the person
        """
        self.name = name
        self.age = age

    def display_info(self):
        """
        Method to display information about the person.
        """
        print(f"Name: {self.name}, Age: {self.age}")
