# Overriding __str__ Method:

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def __str__(self):
        return f"Employee: {self.name}, ID: {self.emp_id}"

# Creating object
emp = Employee("John", 1001)

print(emp)  # Output: Employee: John, ID: 1001
