from pydantic import UUID4, BaseModel, ConfigDict
from datetime import date


class BookDTO(BaseModel):
    """A DTO model for book."""

    id: UUID4
    title: str
    author: str
    published_date: date
    isbn: str
    category: str
    copies_available: int

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )