from pydantic import BaseModel, ConfigDict


class AuthorDTO(BaseModel):
    """A DTO model for author."""

    id: int
    first_name: str
    last_name: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )