# Generator with condition:

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

gen = even_numbers(10)
for num in gen:
    print(num)
# Output:
# 0
# 2
# 4
# 6
# 8
