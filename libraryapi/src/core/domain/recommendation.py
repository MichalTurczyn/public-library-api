from pydantic import UUID4, BaseModel, ConfigDict

class RecommendationIn(BaseModel):
    user_id: UUID4
    recommended_books: list[UUID4]  # lista ID książek
    reason: str  # np. "based on your history with genre: Science Fiction"


class Recommendation(RecommendationIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")