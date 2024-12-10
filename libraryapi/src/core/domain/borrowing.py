from pydantic import UUID4, BaseModel, ConfigDict
from datetime import date, datetime

class BorrowingIn(BaseModel):
    user_id: UUID4
    book_id: UUID4
    borrowed_date: date
    return_date: date | None = None
    returned_date: datetime | None = None


class Borrowing(BorrowingIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")