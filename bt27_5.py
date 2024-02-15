# Handling exceptions with custom messages:

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print("Error:", e)
finally:
    print("Age input operation completed.")