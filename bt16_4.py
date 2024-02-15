# Function with Variable Number of Arguments (Arbitrary Arguments):

def average(*args):
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5))  # Prints 3.0 (average of 1, 2, 3, 4, 5)