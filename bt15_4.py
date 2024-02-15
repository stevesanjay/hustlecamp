# Flattening a list of lists:

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in list_of_lists for num in sublist]
print(flattened_list)