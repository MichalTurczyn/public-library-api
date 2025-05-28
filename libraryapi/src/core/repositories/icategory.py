"""A repository for category entity."""

from abc import ABC, abstractmethod
from typing import Any

from src.core.domain.category import Category, CategoryIn


class ICategoryRepository(ABC):
    """An abstract repository class for category."""

    @abstractmethod
    async def add_category(self, category: CategoryIn) -> Any:
        """Adds a new category to the repository.

        Args:
            category (CategoryIn): The category input data.

        Returns:
            Any: The created category object.
        """

    @abstractmethod
    async def get_category_by_id(self, category_id: int) -> Category | None:
        """Fetches a category by its id.

        Args:
            id (int): id of the category.

        Returns:
            Category | None: The category object if found.
        """

    @abstractmethod
    async def list_categories(self) -> list[Category]:
        """Lists all categories in the repository.

        Returns:
            list[Category]: A list of all categories.
        """

    @abstractmethod
    async def update_category(self, category_id: int, updated_data: CategoryIn) -> Category | None:
        """Updates a category by its ID.

        Args:
            category_id (int): ID of the category to update.
            updated_data (CategoryIn): The updated category data.

        Returns:
            Category | None: The updated category object if successful, otherwise None.
        """

    @abstractmethod
    async def delete_category(self, category_id: int) -> bool:
        """Deletes a category by its ID.

        Args:
            category_id (int): ID of the category to delete.

        Returns:
            bool: True if the category was successfully deleted, otherwise False.
        """