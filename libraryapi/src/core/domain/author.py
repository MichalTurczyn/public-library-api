from pydantic import UUID4, BaseModel, ConfigDict
from datetime import date

class AuthorIn(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date | None = None


class Author(AuthorIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")