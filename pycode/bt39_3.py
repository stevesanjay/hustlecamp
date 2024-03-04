# Creating a Custom Iterator Class:

class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

my_iter = MyIterator(5)

for item in my_iter:
    print(item)
# Output:
# 1
# 2
# 3
# 4
# 5