"""Module containing the implementation of category services."""

from typing import Iterable

from src.core.domain.category import Category, CategoryIn
from src.infrastructure.dto.categorydto import CategoryDTO
from src.infrastructure.services.icategory import ICategoryService
from src.core.repositories.icategory import ICategoryRepository


class CategoryService(ICategoryService):
    """A service class implementing the ICategoryService protocol."""

    _repository: ICategoryRepository
    def __init__(self, repository: ICategoryRepository):
        self._repository = repository

    async def add_category(self, category_data: CategoryIn) -> Category | None:
        return await self._repository.add_category(category_data)

    async def get_category_by_id(self, category_id: int) -> CategoryDTO | None:
        return await self._repository.get_category_by_id(category_id)

    async def list_categories(self) -> Iterable[CategoryDTO]:
        return await self._repository.list_categories()

    async def update_category(
        self, category_id: int, category_data: CategoryIn
    ) -> Category | None:
        return await self._repository.update_category(category_id, category_data)

    async def delete_category(self, category_id: int) -> bool:
        return await self._repository.delete_category(category_id)
