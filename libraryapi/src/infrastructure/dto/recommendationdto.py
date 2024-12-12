from pydantic import UUID4, BaseModel, ConfigDict


class RecommendationDTO(BaseModel):
    """A DTO model for recommendation."""

    id: UUID4
    user_id: UUID4
    recommended_books: list[UUID4]
    reason: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )