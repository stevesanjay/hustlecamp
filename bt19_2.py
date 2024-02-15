# Local Variable:

def print_local():
    y = 20
    print("Local variable y inside function:", y)

print_local()

# This will raise NameError since y is not defined outside the function
# print("Local variable y outside function:", y)