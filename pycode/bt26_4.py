# Writing JSON data to a file:

import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("output.json", "w") as file:
    json.dump(data, file)