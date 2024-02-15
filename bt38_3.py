# Infinite generator:

def infinite_generator():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_generator()
for _ in range(5):
    print(next(gen))
# Output:
# 1
# 2
# 3
# 4
# 5