from sqlalchemy import (MetaData, Table, Column, Integer,
                        String, ForeignKey, DateTime)

from app.db.db import engine

metadata = MetaData()

blogs = Table(
    'blogs', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(250)),
    Column('body', String),
    Column('author', ForeignKey('users.id')),
    Column("created_at", DateTime()),
)

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String, unique=True),
    Column('password', String),
    Column('items', ForeignKey('blogs.author')),
)

tokens = Table(
    'tokens', metadata,
    Column('id', Integer, primary_key=True),
    Column('token', String, unique=True, nullable=False, index=True),
    Column('expires', DateTime()),
    Column('user_id', ForeignKey('users.id')),
)

metadata.create_all(engine)
