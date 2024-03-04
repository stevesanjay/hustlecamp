# Appending data to an existing text file:

with open("output.txt", "a") as file:
    file.write("\nAppending a new line.")