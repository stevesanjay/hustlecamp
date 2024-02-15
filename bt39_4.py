# Using zip() to Iterate over Multiple Iterables:

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

for num, letter in zip(numbers, letters):
    print(num, letter)
# Output:
# 1 a
# 2 b
# 3 c