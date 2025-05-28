from pydantic import BaseModel, ConfigDict
from datetime import date, datetime


class BorrowingDTO(BaseModel):
    """A DTO model for borrowing."""

    id: int
    user_id: int
    book_id: int
    borrowed_date: date
    planned_return_date: date | None = None
    return_date: date | None = None
    status: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )