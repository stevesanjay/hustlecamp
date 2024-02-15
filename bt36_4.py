# _getitem_: Enables accessing elements of an object like a sequence or mapping.


class MyList:
    def __init__(self, *args):
        self.data = list(args)
    
    def __getitem__(self, index):
        return self.data[index]

my_list = MyList(1, 2, 3, 4, 5)
print(my_list[2])  # Output: 3