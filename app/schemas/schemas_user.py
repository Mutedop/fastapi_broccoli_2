from typing import Union
from uuid import UUID

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserBase(BaseModel):
    name: str
    email: str


class UserShow(UserBase):
    id: Union[UUID, int, str]


class UserCreate(UserBase):
    password: str
