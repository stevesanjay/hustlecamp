

from pydantic import BaseModel 
from typing import List , Optional
import json

class Publication(BaseModel):
    publisher: str
    year: int

class Borrower(BaseModel):
    name: str
    borrowDate: str
    returnDate: str

class Book(BaseModel):
    title: str
    author: str
    publication: Publication
    borrowers: List[Borrower]

class Contact(BaseModel):
    phone: str
    email: str

class Library(BaseModel):
    name: str
    address: str
    contact: Contact
    books: List[Book]

class LibraryData(BaseModel):
    library: Library

    # books: Optional[List[dict]]
    # borrowers: Optional[List[dict]]

with open("two.json", "r") as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    try:
        # schema = UserSchema()
        result = LibraryData.parse_obj(json_data)
        print(result)
    except  Exception as e:
        print("error", e)