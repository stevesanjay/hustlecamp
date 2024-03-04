# Overriding __add__ Method:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating vectors
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Adding vectors
result = v1 + v2

print(result)  # Output: (6, 8)