
from pydantic import BaseModel
from typing import List, Dict, Optional
import json 


class Value(BaseModel):
    value: str
    locale: str
    source: str

class Attribute(BaseModel):
    values: List[Value]

class Data(BaseModel):
    attributes: Dict[str, Attribute]

class Properties(BaseModel):
    createdService: str
    createdBy: str
    modifiedService: str
    modifiedBy: str
    createdDate: str
    modifiedDate: str

class DataObject(BaseModel):
    id: str
    type: str
    properties: Properties
    data: Data

class DataObjectOperationResponse(BaseModel):
    status: Optional[str]
    totalRecords: Optional[int]
    dataObjects: Optional[List[DataObject]]


with open("m2.json", "r") as json_file:
    json_data = json.load(json_file)
    print(json_data)
    try:
        result = DataObjectOperationResponse.parse_obj(json_data)
        print(result)
    except  Exception as e:
        print("error", e)

    