"""A repository for category entity."""

from typing import Any
from src.core.domain.category import Category, CategoryIn
from src.core.repositories.icategory import ICategoryRepository
from src.db import category_table, database


class CategoryRepository(ICategoryRepository):
    """A class implementing the database category repository."""

    async def add_category(self, data: CategoryIn) -> Any | None:
        """
        Adds a new category to the database.

        Args:
            data (CategoryIn): The category data to add.

        Returns:
            Any | None: The newly created category if successful, otherwise None.
        """
        query = category_table.insert().values(**data.model_dump())
        new_category_id = await database.execute(query)
        return await self.get_category_by_id(new_category_id)

    async def get_category_by_id(self, category_id: int) -> Any | None:
        """
        Fetches a category record by its ID.

        Args:
            category_id (int): The ID of the category.

        Returns:
            Any | None: The category record if found, otherwise None.
        """
        query = category_table.select().where(category_table.c.id == category_id)
        category = await database.fetch_one(query)
        return Category(**dict(category)) if category else None
    
    async def list_categories(self) -> list[Category]:
        """
        Retrieves all categories from the database.

        Returns:
            list[Category]: A list of all categories.
        """
        query = category_table.select()
        categories = await database.fetch_all(query)
        return [Category(**dict(category)) for category in categories]

    async def update_category(self, category_id: int, data: CategoryIn) -> Any | None:
        """
        Updates an existing category record.

        Args:
            category_id (int): The ID of the category to update.
            data (CategoryIn): The updated category data.

        Returns:
            Any | None: The updated category record if successful, otherwise None.
        """
        query = category_table.update().where(category_table.c.id == category_id).values(**data.model_dump())
        await database.execute(query)
        return await self.get_category_by_id(category_id)

    async def delete_category(self, category_id: int) -> bool:
        """
        Deletes a category record by its ID.

        Args:
            category_id (int): The ID of the category to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        if self.get_category_by_id(id):
            query = category_table.delete().where(category_table.c.id == category_id)
            await database.execute(query)
            return True
        return False