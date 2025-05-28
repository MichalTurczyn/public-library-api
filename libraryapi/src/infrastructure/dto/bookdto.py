from pydantic import BaseModel, ConfigDict


class BookDTO(BaseModel):
    """A DTO model for book."""

    id: int
    title: str
    author_id: int
    published_year: int
    isbn: str
    category_id: int
    copies_available: int

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )