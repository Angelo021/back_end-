from fastapi import APIRouter, HTTPException, Query
from typing import List
from app import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(prefix="/api/books", tags=["Books"])

@router.post("/", response_model=BookResponse, status_code=201)
async def create_book(book: BookCreate):
    book_id = await crud.create_book(book)
    created_book = await crud.get_book(str(book_id))
    if created_book:
        created_book["id"] = str(created_book["_id"])
        return created_book
    raise HTTPException(status_code=500, detail="Failed to create book")

@router.get("/", response_model=List[BookResponse])
async def get_all_books(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=1000)):
    books = await crud.get_all_books(skip, limit)
    for book in books:
        book["id"] = str(book["_id"])
    return books

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: str):
    book = await crud.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book["id"] = str(book["_id"])
    return book

@router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: str, book: BookUpdate):
    updated_book = await crud.update_book(book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found or invalid ID")
    updated_book["id"] = str(updated_book["_id"])
    return updated_book

@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: str):
    deleted = await crud.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return None
