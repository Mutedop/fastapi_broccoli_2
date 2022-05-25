from fastapi import Depends, status, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from app.crud import crud_auth
from app.db import models, db

router = APIRouter(
    prefix='/login',
    tags=['Login'],
)


@router.post('/')
async def login(request: OAuth2PasswordRequestForm = Depends()):
    query = models.users.select().where(
        models.users.c.email == request.username)
    user = await db.database.fetch_one(query)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Login')
    if not crud_auth.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Password')
    access_token = crud_auth.create_access_token(data={'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}
