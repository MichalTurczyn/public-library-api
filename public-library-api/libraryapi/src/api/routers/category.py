from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.domain.category import Category, CategoryIn
from src.infrastructure.services.icategory import ICategoryService

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
@inject
async def add_category(
    category: CategoryIn,
    service: ICategoryService = Depends(Provide[Container.category_service]),
) -> Category:
    """
    Endpoint do dodawania nowej kategorii.

    Args:
        category (CategoryIn): Dane nowej kategorii.
        service (ICategoryService): Serwis do obsługi kategorii.

    Returns:
        Category: Utworzony obiekt kategorii.
    """
    new_category = await service.add_category(category)
    return new_category


@router.get("/{category_id}", response_model=Category, status_code=status.HTTP_200_OK)
@inject
async def get_category_by_uuid(
    category_id: UUID,
    service: ICategoryService = Depends(Provide[Container.category_service]),
) -> Category:
    """
    Endpoint do pobierania kategorii po jej UUID.

    Args:
        category_id (UUID): UUID kategorii.
        service (ICategoryService): Serwis do obsługi kategorii.

    Raises:
        HTTPException: 404 jeśli kategoria nie istnieje.

    Returns:
        Category: Szczegóły kategorii.
    """
    category = await service.get_by_uuid(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category


@router.get("/", response_model=list[Category], status_code=status.HTTP_200_OK)
@inject
async def list_categories(
    service: ICategoryService = Depends(Provide[Container.category_service]),
) -> list[Category]:
    """
    Endpoint do pobierania listy wszystkich kategorii.

    Args:
        service (ICategoryService): Serwis do obsługi kategorii.

    Returns:
        list[Category]: Lista wszystkich kategorii.
    """
    categories = await service.list_categories()
    return categories
