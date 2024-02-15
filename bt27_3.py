# Handling invalid input:

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")
finally:
    print("Input operation completed.")