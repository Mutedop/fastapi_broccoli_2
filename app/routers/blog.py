from fastapi import APIRouter, Path

from app.db import db
from app.db import models
from app.schemas import schemas_blog

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs'],
)


@router.get('/', response_model=list[schemas_blog.BlogShow],
            summary='Read all blogs')
async def read_blogs():
    query = models.blogs.select()
    return await db.database.fetch_all(query)


@router.get('/{blog_id}', response_model=list[schemas_blog.BlogShow])
async def read_blog(
        blog_id: int = Path(
            default=999,
            description='The ID of the blog to get'
        )):
    query = models.blogs.select().where(models.blogs.c.id == blog_id)
    return await db.database.fetch_all(query)


@router.post('/', response_model=schemas_blog.BlogShow,
             summary='Create an item', response_description='The created item')
async def create_blog(item: schemas_blog.BlogCreate):
    """
    Create an item with all the information:

    - **title**: Amazing title of your blog
    - **body**: Unique, unconditional, unpretentious text of your blog
    """
    # = Body(default=None, embed=True)
    query = models.blogs.insert().values(title=item.title, body=item.body)
    record_id = await db.database.execute(query)
    return {**item.dict(), 'id': record_id}


@router.put('/{blog_id}', response_model=schemas_blog.BlogShow)
async def update_blog(blog_id: int, item: schemas_blog.BlogCreate):
    query = models.blogs.update().where(models.blogs.c.id == blog_id).values(
        title=item.title, body=item.body)
    record_id = await db.database.execute(query)
    return {**item.dict(), 'id': record_id}


@router.delete('/{blog_id}')
async def delete_blog(blog_id: int):
    query = models.blogs.delete().where(models.blogs.c.id == blog_id)
    await db.database.execute(query)
    return 'Delete'
