from pydantic import UUID4, BaseModel, ConfigDict
from datetime import datetime

class FineIn(BaseModel):
    user_id: UUID4
    borrowing_id: UUID4
    amount: float
    issued_date: datetime
    paid: bool


class Fine(FineIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")