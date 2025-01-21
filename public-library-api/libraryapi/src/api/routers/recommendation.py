from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.domain.recommendation import Recommendation
from src.infrastructure.services.irecommendation import IRecommendationService

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


@router.get("/{user_id}", response_model=List[Recommendation], status_code=status.HTTP_200_OK)
@inject
async def get_recommendations(
    user_id: str,
    service: IRecommendationService = Depends(Provide[Container.recommendation_service]),
) -> List[Recommendation]:
    """
    Endpoint generujący rekomendacje dla użytkownika.

    Args:
        user_id (str): ID użytkownika, dla którego generowane są rekomendacje.
        service (IRecommendationService): Serwis generujący rekomendacje.

    Raises:
        HTTPException: 404 jeśli rekomendacje nie mogą zostać wygenerowane.

    Returns:
        List[Recommendation]: Lista rekomendacji.
    """
    recommendations = await service.generate_recommendations(user_id)
    if not recommendations:
        raise HTTPException(status_code=404, detail="No recommendations found for this user.")
    return recommendations
