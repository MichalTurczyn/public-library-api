from pydantic import BaseModel, ConfigDict, Field
from datetime import date


class BorrowingIn(BaseModel):
    user_id: int
    book_id: int
    borrowed_date: date
    planned_return_date: date | None = None
    return_date: date = Field(default=date(1900, 1, 1))
    status: str = Field(default="borrowed")


class Borrowing(BorrowingIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="forbid")
