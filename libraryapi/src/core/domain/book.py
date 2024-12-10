from pydantic import UUID4, BaseModel, ConfigDict
from datetime import date

class BookIn(BaseModel):
    title: str
    author: str
    published_date: date
    isbn: str
    copies_available: int



class Book(BookIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")