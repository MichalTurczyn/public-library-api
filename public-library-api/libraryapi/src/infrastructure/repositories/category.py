"""A repository for category entity."""

from typing import Any
from pydantic import UUID4
from src.core.domain.category import Category, CategoryIn
from src.core.repositories.icategory import ICategoryRepository
from src.db import category_table, database


class CategoryRepository(ICategoryRepository):
    """A class implementing the database category repository."""

    async def add_category(self, data: CategoryIn) -> Any | None:
        query = category_table.insert().values(**data.model_dump())
        new_category_id = await database.execute(query)
        return await self.get_by_uuid(new_category_id)

    async def get_by_uuid(self, category_id: UUID4) -> Any | None:
        query = category_table.select().where(category_table.c.id == category_id)
        category = await database.fetch_one(query)
        return Category(**dict(category)) if category else None

    async def update_category(self, category_id: UUID4, data: CategoryIn) -> Any | None:
        query = category_table.update().where(category_table.c.id == category_id).values(**data.model_dump())
        await database.execute(query)
        return await self.get_by_uuid(category_id)

    async def delete_category(self, category_id: UUID4) -> bool:
        query = category_table.delete().where(category_table.c.id == category_id)
        result = await database.execute(query)
        return result > 0

    async def list_categories(self) -> list[Category]:
        query = category_table.select()
        categories = await database.fetch_all(query)
        return [Category(**dict(category)) for category in categories]
