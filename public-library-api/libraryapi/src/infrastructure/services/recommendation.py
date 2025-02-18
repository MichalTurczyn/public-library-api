"""Module containing the implementation of recommendation services."""

from typing import Iterable

from src.core.domain.recommendation import Recommendation
from src.infrastructure.dto.recommendationdto import RecommendationDTO
from src.infrastructure.services.irecommendation import IRecommendationService
from src.core.repositories.irecommendation import IRecommendationRepository


class RecommendationService(IRecommendationService):
    """A service class implementing the IRecommendationService protocol."""

    _repository: IRecommendationRepository

    def __init__(self, repository: IRecommendationRepository) -> None:
        """Initializer for the recommendation service.

        Args:
            repository (IRecommendationRepository): The recommendation repository.
        """
        self._repository = repository

    async def recommend_by_category(self, user_id: int) -> Recommendation:
        """
        Generates book recommendations based on the borrowing history by category.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Recommendation: Recommendations generated for the user based on categories.
        """
        recommendation = await self._repository.recommend_by_category(user_id)
        return RecommendationDTO(
            user_id=recommendation.user_id,
            recommended_books=recommendation.recommended_books,
            reason=recommendation.reason,
        )

    async def recommend_by_author(self, user_id: int) -> Recommendation:
        """
        Generates book recommendations based on the borrowing history by author.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Recommendation: Recommendations generated for the user based on authors.
        """
        recommendation = await self._repository.recommend_by_author(user_id)
        return RecommendationDTO(
            user_id=recommendation.user_id,
            recommended_books=recommendation.recommended_books,
            reason=recommendation.reason,
        )
