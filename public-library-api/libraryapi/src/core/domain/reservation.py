from pydantic import UUID4, BaseModel, ConfigDict
from datetime import datetime
from enum import Enum

class ReservationStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"

class ReservationIn(BaseModel):
    user_id: UUID4
    book_id: UUID4
    reservation_date: datetime
    status: ReservationStatus


class Reservation(ReservationIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")