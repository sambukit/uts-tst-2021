from pydantic import BaseModel, Field, EmailStr

class Pengguna(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        example = {
            "example":{
                "username": "asdf",
                "password": "asdf"
            }
        }