from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4, Field, validator


class UserBase(BaseModel):
    name: str
    email: str
    id: int


class UserShow(UserBase):
    pass


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class TokenBase(BaseModel):
    token: UUID4 = Field(..., alias='access_token')
    expires: datetime
    token_type: Optional[str] = 'bearer'

    class Config:
        allow_population_by_field_name = True

    @validator('token')
    def hexlify_token(cls, value):
        return value.hex


class TokenUser(UserBase):
    token: TokenBase = {}


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None