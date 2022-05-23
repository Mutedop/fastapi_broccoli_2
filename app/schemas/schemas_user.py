from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserShow(UserBase):
    name: str


class UserCreate(UserBase):
    name: str
    email: str
    password: str
