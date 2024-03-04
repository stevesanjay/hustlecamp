# Arbitrary Number of Keyword Arguments:

def greet(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

greet(name="Alice", age=30, city="New York")  
# Output: name : Alice
#         age : 30
#         city : New York