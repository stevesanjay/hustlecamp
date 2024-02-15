# Boolean Short-Circuiting:

def func(a):
    return a > 0

x = 5
y = 0

# Since the first condition is True, the second condition is not evaluated.
result = func(x) and func(y)
print(result)  # False