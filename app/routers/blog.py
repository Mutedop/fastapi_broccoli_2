from fastapi import APIRouter, status, HTTPException, Depends

from app.db import db
from app.db import models
from app.routers.logic import get_current_user
from app.schemas import schemas_blog, schemas_user

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs'],
)


@router.get('/',
            response_model=list[schemas_blog.BlogShow],
            status_code=status.HTTP_200_OK,
            summary='Read all blogs',
            response_description='The read Blogs')
async def read_blogs():
    query = models.blogs.select()
    return await db.database.fetch_all(query)


@router.get('/{blog_id}',
            response_model=schemas_blog.BlogShow,
            status_code=status.HTTP_200_OK,
            summary='Show blog by ID',
            response_description='Show specific blog by ID.')
async def read_blog(blog_id: int):
    """View blog content by entering its ID."""
    query = models.blogs.select().where(models.blogs.c.id == blog_id)
    blog = await db.database.fetch_one(query)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Block for error: blogs id - [ {blog_id} ], not found.'
        )
    return blog


# @router.post('/',
#              response_model=schemas_blog.BlogShow,
#              status_code=status.HTTP_201_CREATED,
#              summary='Create an blog',
#              response_description='The created blog')
# async def create_blog(item: schemas_blog.BlogCreate):
#     """
#     Create a blog with all the information:
#
#     - **title**: Amazing title of your blog
#     - **body**: Unique, unconditional, unpretentious text of your blog
#     """
#     query = models.blogs.insert().values(title=item.title, body=item.body)
#     record_id = await db.database.execute(query)
#     return {**item.dict(), 'id': record_id}


@router.post('/', response_model=schemas_blog.BlogShow)
async def create_blog_owner(item: schemas_blog.BlogCreate,
                            current_user: schemas_user.User = Depends(
                                get_current_user)):
    query = models.blogs.insert().values(
        title=item.title,
        body=item.body,
        author=current_user.email
    )
    record_id = await db.database.execute(query)
    return {**item.dict(), 'id': record_id}


@router.put('/{blog_id}',
            response_model=schemas_blog.BlogShow,
            status_code=status.HTTP_202_ACCEPTED,
            summary='Edit Blog',
            response_description='Edit Blog')
async def update_blog(blog_id: int, item: schemas_blog.BlogCreate):
    query = models.blogs.update().where(models.blogs.c.id == blog_id).values(
        title=item.title, body=item.body)
    record_id = await db.database.execute(query)
    if not record_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Block for error: blogs id - [ {blog_id} ], not found.'
        )
    return {**item.dict(), 'id': record_id}


@router.delete('/{blog_id}',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: int):
    query = models.blogs.delete().where(models.blogs.c.id == blog_id)
    record_id = await db.database.execute(query)
    if not record_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Block for error: blogs id - [ {blog_id} ], not found.'
        )
    return 'Blog [ DELETE ]'
