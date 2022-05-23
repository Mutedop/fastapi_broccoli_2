from databases import Database
from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///./broccoli.db'

database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
