
# Removing Items from a Dictionary:



# Creating an empty dictionary
my_dict = {}

# Adding key-value pairs
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'



# Removing a specific key-value pair
del my_dict['age']
print(my_dict)  # Output: {'name': 'John', 'city': 'New York', 'occupation': 'Engineer'}

# Removing all items
my_dict.clear()
print(my_dict)  # Output: {}
