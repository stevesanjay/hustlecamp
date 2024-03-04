# Writing data from a list to a CSV file:

import csv

data = [
    ["Name", "Age", "Country"],
    ["Alice", 25, "USA"],
    ["Bob", 30, "UK"],
    ["Charlie", 35, "Canada"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)