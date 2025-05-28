from pydantic import BaseModel, ConfigDict


class RecommendationDTO(BaseModel):
    """A DTO model for recommendation."""
    user_id: int
    recommended_books: list[int]
    reason: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )