from pydantic import UUID4, BaseModel, ConfigDict
from datetime import datetime


class ReservationDTO(BaseModel):
    """A DTO model for reservation."""

    id: UUID4
    user_id: UUID4
    book_id: UUID4
    reservation_date: datetime
    status: str  # pending, confirmed, canceled

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )