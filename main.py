from fastapi import FastAPI

from app.db import db
from app.routers import routers_user, routers_blog, routers_auth
from description import tags_metadata, description

app = FastAPI(
    openapi_tags=tags_metadata,
    title='Broccoli',
    description=description,
    version='2.0.1',
    contact={
        'name': 'Pavel P.',
        'github': 'https://github.com/Mutedop',
    },
    license_info={
        'name': 'MIT License'
    },
)

app.include_router(routers_blog.router)
app.include_router(routers_user.router)
app.include_router(routers_auth.router)


@app.on_event('startup')
async def startup():
    await db.database.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.database.disconnect()
