
from marshmallow import Schema, fields 
import json

# class UserSchema(Schema):
#     name = fields.Str()
#     age = fields.Int()
#     hobbies = fields.List(fields.Str())

# with open("one.json", "r") as json_file:
#     json_data = json.load(json_file)
#     print(json_data)

#     schema = UserSchema()
#     result = schema.load(json_data)
#     print(result)
        
# class UserSchemaOne(Schema):
#     library = fields.Dict()
#     books   = fields.List(fields.Dict())

# with open("two.json", "r") as json_file:
#         json_data = json.load(json_file)
#         # print(json_data)

#         schema = UserSchemaOne()
#         result = schema.load(json_data)
#         print(result)

class UserSchemaOne(Schema):
    dataObjectOperationResponse = fields.Dict()
    data   = fields.List(fields.Dict())

with open("three.json", "r") as json_file:
        json_data = json.load(json_file)
        # print(json_data)

        schema = UserSchemaOne()
        result = schema.load(json_data)
        print(result)
