from typing import Optional
from pydantic import BaseModel, Field


class BlogBase(BaseModel):
    title: Optional[str] = Field(example='Title Blog')
    body: Optional[str] = Field(example='Text Blog')


class BlogCreate(BlogBase):
    title: str
    body: str


class BlogShow(BlogBase):
    pass


class BlogInDB(BlogBase):
    id: int
    title: str
    body: str
    author: int
