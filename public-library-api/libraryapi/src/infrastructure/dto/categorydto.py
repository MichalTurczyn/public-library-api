from pydantic import BaseModel, ConfigDict


class CategoryDTO(BaseModel):
    """A DTO model for category."""

    id: int
    name: str
    description: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )