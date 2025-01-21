"""A repository for recommendation entity."""

from abc import ABC, abstractmethod

from src.core.domain.recommendation import Recommendation


class IRecommendationRepository(ABC):
    """An abstract repository class for recommendation."""

    @abstractmethod
    async def generate_recommendations(self, user_id: str) -> list[Recommendation]:
        """Generates recommendations for a user.

        Args:
            user_id (str): The user's ID.

        Returns:
            list[Recommendation]: A list of recommendations.
        """
