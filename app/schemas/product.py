from pydantic import BaseModel,ConfigDict,Field
class ProductCreate(BaseModel):
    name:str
    description:str|None=None
    price:float=Field(ge=0)
    quantity:int=Field(ge=0)
    
class ProductResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:int
    name:str
    description:str|None=None
    price:float
    quantity:int
    model_config=ConfigDict(from_attributes=True)