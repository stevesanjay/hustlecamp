# Recursion - Function Calling Itself:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Prints 120 (5! = 5 * 4 * 3 * 2 * 1)