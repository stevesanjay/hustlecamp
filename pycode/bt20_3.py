# Lambda function as an argument to another function:

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use lambda function with the map() function to double each number in the list
doubled_numbers = list(map(lambda x: x * 2, numbers))

# Print the result
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]