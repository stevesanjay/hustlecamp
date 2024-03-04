# Modifying Global Variable Inside a Function:

x = 10

def modify_global():
    global x
    x = 50
    print("Modified global variable x inside function:", x)

modify_global()
print("Global variable x after modification:", x)