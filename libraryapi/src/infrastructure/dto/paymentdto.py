from pydantic import UUID4, BaseModel, ConfigDict
from datetime import datetime


class PaymentDTO(BaseModel):
    """A DTO model for payment."""

    id: UUID4
    user_id: UUID4
    amount: float
    payment_date: datetime
    description: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )