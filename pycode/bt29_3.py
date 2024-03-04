
# Class Variables:

class Employee:
    raise_amount = 1.05  # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary *= self.raise_amount

emp1 = Employee("Alice", 50000)
print(emp1.salary)
emp1.apply_raise()
print(emp1.salary)
