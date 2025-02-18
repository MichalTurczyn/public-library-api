from pydantic import BaseModel, ConfigDict


class UserDTO(BaseModel):
    """A DTO model for user."""

    id: int
    email: str
    password: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )