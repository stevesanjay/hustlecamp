# _str_: Defines the string representation of an object.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(str(p))  # Output: (3, 4)