# from marshmallow import Schema, fields
from pydantic import BaseModel 
from typing import List
import json

class User(BaseModel):
    name: tr
    age :int
    hobbies : List[str]

with open("one.json", "r") as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    try:
        result = User.parse_obj(json_data)
        print(result)
    except  Exception as e:
        print("error", e)






    