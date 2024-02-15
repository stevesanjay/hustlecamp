# Accessing Values in a Dictionary:


# Creating an empty dictionary
my_dict = {}

# Adding key-value pairs
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'


# Accessing values using keys
print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 30

# Accessing a non-existent key
print(my_dict.get('occupation'))  # Output: None