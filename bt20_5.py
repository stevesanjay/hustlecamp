# Sorting a list of tuples by the second element using a lambda function:

# Define a list of tuples
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]

# Sort the list of tuples by the second element using a lambda function
sorted_pairs = sorted(pairs, key=lambda x: x[1])

# Print the sorted list
print(sorted_pairs)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]