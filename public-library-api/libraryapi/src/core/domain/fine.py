from pydantic import UUID4, BaseModel, ConfigDict, Field
from datetime import datetime

class FineIn(BaseModel):
    user_id: UUID4
    borrowing_id: UUID4
    amount: float = Field(gt=0)
    issued_date: datetime
    paid: bool


class Fine(FineIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")