from pydantic import UUID4, BaseModel, ConfigDict
from datetime import datetime

class PaymentIn(BaseModel):
    user_id: UUID4
    amount: float
    payment_date: datetime
    description: str | None = None


class Payment(PaymentIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")