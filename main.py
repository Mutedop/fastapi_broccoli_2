from fastapi import FastAPI

from app.db import db
from app.routers import blog, user
from description import tags_metadata, description

app = FastAPI(
    openapi_tags=tags_metadata,
    title='Broccoli',
    description=description,
    version='2.0.1',
    contact={
        'name': 'Mutedop',
        'github': 'https://github.com/Mutedop',
    },
    license_info={
        'name': 'MIT License'
    },
)

app.include_router(blog.router)
app.include_router(user.router)


@app.on_event('startup')
async def startup():
    await db.database.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.database.disconnect()
