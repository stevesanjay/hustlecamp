# Arbitrary Number of Arguments (Positional):

def greet(*names):
    for name in names:
        print("Hello,", name)

greet("Alice", "Bob", "Charlie")  # Output: Hello, Alice
                                  #         Hello, Bob
                                  #         Hello, Charlie