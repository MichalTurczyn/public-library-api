"""A repository for category entity."""

from abc import ABC, abstractmethod
from typing import Any
from pydantic import UUID4

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
    async def get_by_uuid(self, uuid: UUID4) -> Category | None:
        """Fetches a category by its UUID.

        Args:
            uuid (UUID4): UUID of the category.

        Returns:
            Category | None: The category object if found.
        """

    @abstractmethod
    async def list_categories(self) -> list[Category]:
        """Lists all categories in the repository.

        Returns:
            list[Category]: A list of all categories.
        """
