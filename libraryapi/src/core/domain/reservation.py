from pydantic import UUID4, BaseModel, ConfigDict
from datetime import datetime

class ReservationIn(BaseModel):
    user_id: UUID4
    book_id: UUID4
    reservation_date: datetime
    status: str  # pending, confirmed, canceled


class Reservation(ReservationIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")