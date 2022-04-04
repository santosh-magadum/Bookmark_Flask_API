from pydantic import BaseModel


class userCreate(BaseModel):
    email:str
    password:str
    username:str