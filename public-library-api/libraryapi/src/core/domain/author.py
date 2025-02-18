from pydantic import BaseModel, ConfigDict

class AuthorIn(BaseModel):
    first_name: str
    last_name: str


class Author(AuthorIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")