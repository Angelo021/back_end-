
from bson import ObjectId
from app.database import book_collection
from app.schemas import BookCreate, BookUpdate
from datetime import datetime

async def create_book(book: BookCreate):
    book_dict = book.model_dump()
    book_dict["created_at"] = datetime.now()
    book_dict["updated_at"] = datetime.now()
    result = await book_collection.insert_one(book_dict)
    return result.inserted_id

async def get_book(book_id: str):
    if not ObjectId.is_valid(book_id):
        return None
    book = await book_collection.find_one({"_id": ObjectId(book_id)})
    return book

async def get_all_books(skip: int = 0, limit: int = 100):
    cursor = book_collection.find().skip(skip).limit(limit)
    books = await cursor.to_list(length=limit)
    return books

async def update_book(book_id: str, book: BookUpdate):
    if not ObjectId.is_valid(book_id):
        return None
    
    update_data = book.model_dump(exclude_unset=True)
    if update_data:
        update_data["updated_at"] = datetime.now()
        result = await book_collection.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": update_data}
        )
        if result.modified_count > 0:
            return await get_book(book_id)
    return None

async def delete_book(book_id: str):
    if not ObjectId.is_valid(book_id):
        return False
    result = await book_collection.delete_one({"_id": ObjectId(book_id)})
    return result.deleted_count > 0
