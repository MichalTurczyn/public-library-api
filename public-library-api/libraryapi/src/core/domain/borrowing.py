from pydantic import UUID4, BaseModel, ConfigDict
from datetime import date, datetime


class BorrowingIn(BaseModel):
    """
    Input data model for borrowing.
    """
    user_id: UUID4
    book_id: UUID4
    borrowed_date: date
    return_date: date | None = None
    returned_date: datetime | None = None


class Borrowing(BorrowingIn):
    """
    Represents a borrowing record, extended with an ID field.
    """
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="forbid")

    @classmethod
    def from_data(cls, data: dict) -> "Borrowing":
        """
        Creates a Borrowing instance after validating and processing input data.

        Args:
            data (dict): Input data for borrowing.

        Returns:
            Borrowing: An instance of the Borrowing class.

        Raises:
            ValueError: If returned_date is earlier than borrowed_date.
        """
        borrowed_date = data.get("borrowed_date")
        returned_date = data.get("returned_date")

        if returned_date and returned_date < datetime.combine(borrowed_date, datetime.min.time()):
            raise ValueError("Returned date cannot be earlier than borrowed date")

        return cls(**data)
