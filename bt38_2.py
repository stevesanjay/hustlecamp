# Generator expression:

gen = (x ** 2 for x in range(5))
for num in gen:
    print(num)
# Output:
# 0
# 1
# 4
# 9
# 16