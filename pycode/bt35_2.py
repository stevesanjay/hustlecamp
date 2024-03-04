
# Polymorphic Functions:

def add(x, y):
    return x + y

def concatenate(x, y):
    return str(x) + str(y)

# Polymorphic function
print(add(5, 10))        # Output: 15
print(add("Hello", " ")) # Output: Hello 
print(concatenate(5, 10)) # Output: 510
print(concatenate("Hello", " ")) # Output: Hello