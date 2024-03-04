# Nonlocal Keyword:

def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
        print("Modified variable x inside inner function:", x)

    inner()
    print("Variable x after modification inside inner function:", x)

outer()