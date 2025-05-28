"""Module containing recommendation service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.recommendation import Recommendation


class IRecommendationService(ABC):
    """An abstract class representing the protocol for recommendation services."""

    @abstractmethod
    async def recommend_by_category(self, user_id: int) -> Recommendation:
        """
        Generates book recommendations based on the borrowing history by category.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Recommendation: Recommendations generated for the user based on categories.
        """
        pass

    @abstractmethod
    async def recommend_by_author(self, user_id: int) -> Recommendation:
        """
        Generates book recommendations based on the borrowing history by author.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Recommendation: Recommendations generated for the user based on authors.
        """
        pass
