
# Iterating Over a Dictionary:



# Creating an empty dictionary
my_dict = {}

# Adding key-value pairs
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'


# Iterating over keys
for key in my_dict:
    print(key)  # Output: name, age, city, occupation

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, ":", value)
