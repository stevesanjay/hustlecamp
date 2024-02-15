# Using Context Managers for File I/O:

# Reading from a file using context manager
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Strip newline character

# Writing to a file using context manager
with open('output.txt', 'w') as f:
    f.write('Some content here.\n')