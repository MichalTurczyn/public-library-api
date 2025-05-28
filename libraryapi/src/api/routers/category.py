from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.domain.category import Category, CategoryIn
from src.infrastructure.services.icategory import ICategoryService

router = APIRouter(prefix="/Category", tags=["Category"])


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
@inject
async def add_category(
    category: CategoryIn,
    service: ICategoryService = Depends(Provide[Container.category_service]),
) -> Category:
    new_category = await service.add_category(category)
    return new_category


@router.get("/{category_id}", response_model=Category, status_code=status.HTTP_200_OK)
@inject
async def get_category_by_id(
    category_id: int,
    service: ICategoryService = Depends(Provide[Container.category_service]),
) -> Category:
    category = await service.get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category


@router.get("/", response_model=list[Category], status_code=status.HTTP_200_OK)
@inject
async def list_categories(
    service: ICategoryService = Depends(Provide[Container.category_service]),
) -> list[Category]:
    categories = await service.list_categories()
    return categories

@router.put("/{category_id}", response_model=Category, status_code=status.HTTP_200_OK)
@inject
async def update_category(
    category_id: int,
    updated_data: CategoryIn,
    service: ICategoryService = Depends(Provide[Container.category_service]),
) -> Category:
    category = await service.update_category(category_id, updated_data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_category(
    category_id: int,
    service: ICategoryService = Depends(Provide[Container.category_service]),
):
    success = await service.delete_category(category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found.")