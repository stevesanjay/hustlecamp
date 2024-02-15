# _init_: The constructor method, called when an object is created.


class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(obj.value)  # Output: 10