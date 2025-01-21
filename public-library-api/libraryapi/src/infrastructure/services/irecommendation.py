"""Module containing recommendation service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable
from pydantic import UUID4

from src.core.domain.recommendation import Recommendation, RecommendationIn
from src.infrastructure.dto.recommendationdto import RecommendationDTO


class IRecommendationService(ABC):
    """An abstract class representing the protocol for recommendation services."""

    @abstractmethod
    async def add_recommendation(self, data: RecommendationIn) -> Recommendation | None:
        """Adds a new recommendation to the repository.

        Args:
            data (RecommendationIn): The details of the recommendation.

        Returns:
            Recommendation | None: The newly created recommendation.
        """

    @abstractmethod
    async def get_recommendation_by_id(self, recommendation_id: UUID4) -> RecommendationDTO | None:
        """Fetches a recommendation by its UUID.

        Args:
            recommendation_id (UUID4): The UUID of the recommendation.

        Returns:
            RecommendationDTO | None: The recommendation details if found.
        """

    @abstractmethod
    async def list_recommendations(self) -> Iterable[RecommendationDTO]:
        """Lists all recommendations.

        Returns:
            Iterable[RecommendationDTO]: A collection of all recommendations.
        """

    @abstractmethod
    async def update_recommendation(
        self,
        recommendation_id: UUID4,
        data: RecommendationIn,
    ) -> Recommendation | None:
        """Updates an existing recommendation.

        Args:
            recommendation_id (UUID4): The UUID of the recommendation to update.
            data (RecommendationIn): The updated recommendation details.

        Returns:
            Recommendation | None: The updated recommendation.
        """

    @abstractmethod
    async def delete_recommendation(self, recommendation_id: UUID4) -> bool:
        """Deletes a recommendation by its UUID.

        Args:
            recommendation_id (UUID4): The UUID of the recommendation to delete.

        Returns:
            bool: True if deletion was successful, otherwise False.
        """

    @abstractmethod
    async def get_recommendations_for_user(self, user_id: UUID4) -> Iterable[RecommendationDTO]:
        """Fetches recommendations for a specific user.

        Args:
            user_id (UUID4): The UUID of the user.

        Returns:
            Iterable[RecommendationDTO]: A collection of recommendations for the user.
        """
