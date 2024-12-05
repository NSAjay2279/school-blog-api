from fastapi import FastAPI
from app.config import get_mongo_client
from app.routes import router
from app.config import get_mongo_client

app = FastAPI()

# Get the MongoDB client
client = get_mongo_client()
db = client["your_database_name"]  # Replace with your database name

app.include_router(router)
