"""A repository for recommendation entity."""

from abc import ABC, abstractmethod

from src.core.domain.recommendation import Recommendation


class IRecommendationRepository(ABC):
    """An abstract repository class for recommendation."""

    @abstractmethod
    async def recommend_by_category(self, user_id: int) -> Recommendation:
        """
        Generates book recommendations based on the borrowing history by category.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Recommendation: Recommendations generated for the user based on categories.
        """

    @abstractmethod
    async def recommend_by_author(self, user_id: int) -> Recommendation:
        """
        Generates book recommendations based on the borrowing history by author.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Recommendation: Recommendations generated for the user based on authors.
        """