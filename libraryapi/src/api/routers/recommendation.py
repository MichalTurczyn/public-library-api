from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.domain.recommendation import Recommendation
from src.infrastructure.services.irecommendation import IRecommendationService

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


@router.get("/by-category/{user_id}", response_model=Recommendation, status_code=200)
@inject
async def recommend_by_category(
    user_id: int,
    service: IRecommendationService = Depends(Provide[Container.recommendation_service]),
) -> Recommendation:
    recommendations = await service.recommend_by_category(user_id)
    if not recommendations.recommended_books:
        raise HTTPException(status_code=404, detail="No recommendations found for this user.")
    return recommendations


@router.get("/by-author/{user_id}", response_model=Recommendation, status_code=200)
@inject
async def recommend_by_author(
    user_id: int,
    service: IRecommendationService = Depends(Provide[Container.recommendation_service]),
) -> Recommendation:
    recommendations = await service.recommend_by_author(user_id)
    if not recommendations.recommended_books:
        raise HTTPException(status_code=404, detail="No recommendations found for this user.")
    return recommendations