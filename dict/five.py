# How do you remove a key-value pair from a dictionary?

# pop
# delete

my_dict = {
    'apple' : 2,
    'banana': 3,
    'orange': 4,
    'mango' : 5
    }

del my_dict["apple"]
print(my_dict)





'''
output:
    {'banana': 3, 'orange': 4, 'mango': 5}
'''