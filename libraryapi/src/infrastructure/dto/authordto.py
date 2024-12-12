from pydantic import UUID4, BaseModel, ConfigDict


class AuthorDTO(BaseModel):
    """A DTO model for author."""

    id: UUID4
    first_name: str
    last_name: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )