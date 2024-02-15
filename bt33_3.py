# Overriding Built-in Methods:

class MyList(list):
    def append(self, element):
        print("Appending element:", element)
        super().append(element)

# Creating object
my_list = MyList()

# Appending elements
my_list.append(1)
my_list.append(2)
# Output:
# Appending element: 1
# Appending element: 2

print(my_list)  # Output: [1, 2]