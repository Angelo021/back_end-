from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "book_db")

client = AsyncIOMotorClient(MONGO_URI)
database = client[MONGO_DB]
book_collection = database.get_collection("books")
