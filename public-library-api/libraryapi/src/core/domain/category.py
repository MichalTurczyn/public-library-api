from pydantic import BaseModel, ConfigDict

class CategoryIn(BaseModel):
    name: str
    description: str | None = None


class Category(CategoryIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")