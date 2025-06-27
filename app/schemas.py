from pydantic import BaseModel,EmailStr
from datetime import datetime

class UserPost(BaseModel):
    email:EmailStr
    title:str
    blog:str

class UpdatePost(BaseModel):
    title:str
    blog:str

    model_config = {
        "extra": "forbid"
    }
    
class Postresponse(BaseModel):
    id:int
    title:str
    blog:str
    created_at:datetime

    class Config:
        orm_mode=True


class UpdatePostResponse(Postresponse):
    email:EmailStr

    class Config:
        orm_mode=True


