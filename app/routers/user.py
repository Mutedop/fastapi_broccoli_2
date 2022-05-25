from fastapi import APIRouter

from app.db import models, db
from app.routers.logic import get_password_hash
from app.schemas import schemas_user

router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@router.get('/', response_model=list[schemas_user.UserShow])
async def read_users():
    query = models.users.select()
    return await db.database.fetch_all(query)


@router.get('/{user_id}', response_model=list[schemas_user.UserShow])
async def read_user(user_id: int):
    query = models.users.select().where(models.users.c.id == user_id)
    return await db.database.fetch_one(query)


@router.post('/', response_model=schemas_user.UserShow)
async def create_user(item: schemas_user.UserCreate):
    query = models.users.insert().values(
        name=item.name,
        password=get_password_hash(item.password),
        email=item.email
    )
    record_id = await db.database.execute(query)
    return {**item.dict(), 'id': record_id}
