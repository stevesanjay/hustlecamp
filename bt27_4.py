# Handling key errors in dictionaries:

my_dict = {"a": 1, "b": 2, "c": 3}
try:
    value = my_dict["d"]
except KeyError:
    print("Error: Key not found in dictionary!")
finally:
    print("Dictionary access operation completed.")