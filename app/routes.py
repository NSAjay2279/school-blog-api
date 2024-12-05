from fastapi import APIRouter, HTTPException
from app.models import Post

router = APIRouter()


@router.post("/posts/")
async def create_post(post: Post):
    # Insert the post into the MongoDB collection
    result = await db.posts.insert_one(post.dict())
    return {"inserted_id": str(result.inserted_id)}


@router.get("/posts/")
async def get_posts():
    posts = await db.posts.find().to_list(length=None)
    return posts
