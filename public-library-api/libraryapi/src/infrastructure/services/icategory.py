"""Module containing category service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable
from pydantic import UUID4

from src.core.domain.category import Category, CategoryIn
from src.infrastructure.dto.categorydto import CategoryDTO


class ICategoryService(ABC):
    """An abstract class representing the protocol for category services."""

    @abstractmethod
    async def add_category(self, category_data: CategoryIn) -> Category | None:
        """Adds a new category to the repository.

        Args:
            category_data (CategoryIn): The details of the category.

        Returns:
            Category | None: The newly created category.
        """

    @abstractmethod
    async def get_category_by_id(self, category_id: UUID4) -> CategoryDTO | None:
        """Fetches a category using its UUID.

        Args:
            category_id (UUID4): The UUID of the category.

        Returns:
            CategoryDTO | None: The category details if found.
        """

    @abstractmethod
    async def list_categories(self) -> Iterable[CategoryDTO]:
        """Lists all categories.

        Returns:
            Iterable[CategoryDTO]: A collection of all categories.
        """

    @abstractmethod
    async def update_category(
        self, category_id: UUID4, category_data: CategoryIn
    ) -> Category | None:
        """Updates an existing category.

        Args:
            category_id (UUID4): The UUID of the category to update.
            category_data (CategoryIn): The updated category details.

        Returns:
            Category | None: The updated category if successful.
        """

    @abstractmethod
    async def delete_category(self, category_id: UUID4) -> bool:
        """Deletes a category by its UUID.

        Args:
            category_id (UUID4): The UUID of the category to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
