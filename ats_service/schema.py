from pydantic import BaseModel


# Define a request body using Pydantic
class Item(BaseModel):
    first: int
    second: int
   

class SumResponse(BaseModel):
    sum : int