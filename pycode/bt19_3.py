# Nested Functions and Scope:

def outer_function():
    a = 30

    def inner_function():
        print("Variable a inside inner_function:", a)

    inner_function()

# Variable a inside inner_function can access the variable defined in outer_function
outer_function()