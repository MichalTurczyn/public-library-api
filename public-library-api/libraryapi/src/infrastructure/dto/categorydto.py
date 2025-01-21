from pydantic import UUID4, BaseModel, ConfigDict


class CategoryDTO(BaseModel):
    """A DTO model for category."""

    id: UUID4
    name: str
    description: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )