from pydantic import UUID4, BaseModel, ConfigDict, Field

class RecommendationIn(BaseModel):
    user_id: UUID4
    recommended_books: list[UUID4] = Field(min_items=1)
    reason: str


class Recommendation(RecommendationIn):
    id: UUID4

    model_config = ConfigDict(from_attributes=True, extra="ignore")