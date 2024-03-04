# _len_: Defines the behavior of the len() function for objects.


class MyCustomList:
    def __init__(self, *args):
        self.data = list(args)
    
    def __len__(self):
        return len(self.data)

custom_list = MyCustomList(1, 2, 3, 4, 5)
print(len(custom_list))  # Output: 5