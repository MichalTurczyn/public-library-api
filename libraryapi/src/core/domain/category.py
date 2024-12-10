from pydantic import UUID4, BaseModel, ConfigDict

class CategoryIn(BaseModel):
    name: str
    description: str | None = None


class Category(CategoryIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")