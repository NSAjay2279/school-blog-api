from fastapi import FastAPI
from app.config import get_mongo_client

app = FastAPI()

# Get the MongoDB client
client = get_mongo_client()
db = client["school_blog"]
blogs_collection = db["blogs"]
users_collection = db["users"]

# ... rest of your application logic


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Other API endpoints
