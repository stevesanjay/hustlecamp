# Search for Element in List:

def find_element(lst, element):
    return element in lst

my_list = [1, 2, 3, 4, 5]
print(find_element(my_list, 3))  # Output: True
print(find_element(my_list, 6))  # Output: False