# Handling division by zero:

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")
