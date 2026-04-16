from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class BookModel(BaseModel):
    title: str
    author: str
    year: int
    genre: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
