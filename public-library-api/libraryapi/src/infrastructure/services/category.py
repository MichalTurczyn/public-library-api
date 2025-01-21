"""Module containing the implementation of category services."""

from typing import Iterable
from pydantic import UUID4

from src.core.domain.category import Category, CategoryIn
from src.infrastructure.dto.categorydto import CategoryDTO
from src.infrastructure.services.icategory import ICategoryService


class CategoryService(ICategoryService):
    """A service class implementing the ICategoryService protocol."""

    async def add_category(self, category_data: CategoryIn) -> Category | None:
        """Adds a new category to the repository."""
        # Implementation logic for adding a category
        pass

    async def get_category_by_id(self, category_id: UUID4) -> CategoryDTO | None:
        """Fetches a category using its UUID."""
        # Implementation logic for fetching a category by UUID
        pass

    async def list_categories(self) -> Iterable[CategoryDTO]:
        """Lists all categories."""
        # Implementation logic for listing all categories
        pass

    async def update_category(
        self, category_id: UUID4, category_data: CategoryIn
    ) -> Category | None:
        """Updates an existing category."""
        # Implementation logic for updating a category
        pass

    async def delete_category(self, category_id: UUID4) -> bool:
        """Deletes a category by its UUID."""
        # Implementation logic for deleting a category
        pass
