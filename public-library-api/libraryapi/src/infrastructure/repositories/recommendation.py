"""A repository for recommendation entity."""

from typing import Any, Iterable
from pydantic import UUID4
from src.core.domain.recommendation import Recommendation
from src.core.repositories.irecommendation import IRecommendationRepository
from src.db import recommendation_table, database


class RecommendationRepository(IRecommendationRepository):
    """A class implementing the database recommendation repository."""

    async def get_recommendations_for_user(self, user_id: UUID4) -> Iterable[Any]:
        query = recommendation_table.select().where(recommendation_table.c.user_id == user_id)
        recommendations = await database.fetch_all(query)
        return [Recommendation(**dict(recommendation)) for recommendation in recommendations]

    async def add_recommendation(self, recommendation_data: dict) -> Any | None:
        query = recommendation_table.insert().values(**recommendation_data)
        new_recommendation_id = await database.execute(query)
        query = recommendation_table.select().where(recommendation_table.c.id == new_recommendation_id)
        recommendation = await database.fetch_one(query)
        return Recommendation(**dict(recommendation)) if recommendation else None
