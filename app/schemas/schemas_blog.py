from typing import Optional, Union
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class BlogBase(BaseModel):
    title: Optional[str] = Field(example='Title Blog', max_length=300)
    body: Optional[str] = Field(example='Text Blog')


class BlogCreate(BlogBase):
    pass


class BlogShow(BlogBase):
    id: Union[UUID, int, str]


class BlogShowFull(BlogBase):
    id: Union[UUID, int, str]
    created_at: datetime
    author: str
