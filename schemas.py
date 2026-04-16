from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    year: int = Field(..., ge=1450, le=2024)
    genre: str = Field(..., min_length=1, max_length=50)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    year: Optional[int] = Field(None, ge=1450, le=2024)
    genre: Optional[str] = Field(None, min_length=1, max_length=50)

class BookInDB(BookBase):
    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

class BookResponse(BookBase):
    id: str
    created_at: datetime
    updated_at: datetime
