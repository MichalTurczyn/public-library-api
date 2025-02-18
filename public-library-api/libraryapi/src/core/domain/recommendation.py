from pydantic import BaseModel, ConfigDict, Field

class RecommendationIn(BaseModel):
    user_id: int
    recommended_books: list[int] = Field(min_items=1)
    reason: str


class Recommendation(RecommendationIn):

    model_config = ConfigDict(from_attributes=True, extra="ignore")