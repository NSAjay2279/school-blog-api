from fastapi import FastAPI
from pymongo import MongoClient
from app.routes import router

app = FastAPI()

# Replace with your actual MongoDB connection string
client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]

app.include_router(router)
