from pydantic import UUID4, BaseModel, ConfigDict
from datetime import datetime


class FineDTO(BaseModel):
    """A DTO model for fine."""

    id: UUID4
    user_id: UUID4
    borrowing_id: UUID4
    amount: float
    issued_date: datetime
    paid: bool

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )