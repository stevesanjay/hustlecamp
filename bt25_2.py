# Reading File Line by Line:

with open('filename.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters