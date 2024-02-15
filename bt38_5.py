# Chaining generators:

def generator1():
    for i in range(5):
        yield i

def generator2():
    for i in range(5, 10):
        yield i

gen1 = generator1()
gen2 = generator2()

for num in gen1:
    print(num)

for num in gen2:
    print(num)
# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9