from pydantic import BaseModel, ConfigDict


class BookIn(BaseModel):
    title: str
    author_id: int
    published_year: int
    isbn: str
    category_id: int
    copies_available: int



class Book(BookIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")