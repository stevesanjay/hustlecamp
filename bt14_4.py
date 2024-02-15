# Printing a Pascal's triangle:

rows = 5
for i in range(rows):
    coef = 1
    for j in range(1, rows - i):
        print(" ", end="")
    for k in range(0, i + 1):
        print(coef, end="")
        coef = coef * (i - k) // (k + 1)
    print()
