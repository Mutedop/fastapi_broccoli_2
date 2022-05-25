from typing import Optional
from pydantic import BaseModel, Field


class BlogBase(BaseModel):
    title: Optional[str] = Field(example='Title Blog', max_length=300)
    body: Optional[str] = Field(example='Text Blog')


class BlogCreate(BlogBase):
    pass


class BlogShow(BlogBase):
    id: str
