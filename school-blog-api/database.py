from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"  # Replace with your MongoDB URI
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client["school_blog"]
