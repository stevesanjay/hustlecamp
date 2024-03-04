# Reading Limited Characters:

with open('filename.txt', 'r') as file:
    content = file.read(100)  # Read the first 100 characters
    print(content)