from pydantic import BaseModel 
from typing import List , Optional
import json



class UserSchemaOne(BaseModel):

    dataObjectOperationResponse: dict
    # data: Optional.List[fields.Dict]

with open("three.json", "r") as json_file:
        json_data = json.load(json_file)
        # print(json_data)

        # schema = UserSchemaOne()
        result = UserSchemaOne.parse_obj(json_data)
        print(result)
