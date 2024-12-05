from fastapi import FastAPI, HTTPException
from models import Blog
from database import db
from schemas import BlogCreate, BlogResponse
from bson import ObjectId

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the School Blog API"}

@app.post("/blogs", response_model=BlogResponse)
async def create_blog(blog: BlogCreate):
    new_blog = await db["blogs"].insert_one(blog.dict())
    created_blog = await db["blogs"].find_one({"_id": new_blog.inserted_id})
    return Blog(**created_blog)

@app.get("/blogs/{id}", response_model=BlogResponse)
async def get_blog(id: str):
    blog = await db["blogs"].find_one({"_id": ObjectId(id)})
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return Blog(**blog)

@app.delete("/blogs/{id}")
async def delete_blog(id: str):
    result = await db["blogs"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted successfully"}
