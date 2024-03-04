# Reading Lines from a File:

# Open file in read mode
with open('file.txt', 'r') as f:
    # Read lines from file
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # Strip newline character