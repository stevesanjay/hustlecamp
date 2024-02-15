# Reading Lines into a List:

with open('filename.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
