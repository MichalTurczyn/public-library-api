"""A repository for fine entity."""

from typing import Any
from pydantic import UUID4
from src.core.domain.fine import Fine, FineIn
from src.core.repositories.ifine import IFineRepository
from src.db import fine_table, database


class FineRepository(IFineRepository):
    """A class implementing the database fine repository."""

    async def add_fine(self, data: FineIn) -> Any | None:
        query = fine_table.insert().values(**data.model_dump())
        new_fine_id = await database.execute(query)
        fine = await self.get_by_uuid(new_fine_id)
        return fine

    async def get_fine_by_user(self, user_id: UUID4) -> list[Fine]:
        query = fine_table.select().where(fine_table.c.user_id == user_id)
        fines = await database.fetch_all(query)
        return [Fine(**dict(fine)) for fine in fines]

    async def pay_fine(self, fine_id: UUID4) -> bool:
        query = fine_table.update().where(fine_table.c.id == fine_id).values(is_paid=True)
        result = await database.execute(query)
        return result > 0

    async def get_by_uuid(self, fine_id: UUID4) -> Any | None:
        query = fine_table.select().where(fine_table.c.id == fine_id)
        fine = await database.fetch_one(query)
        return Fine(**dict(fine)) if fine else None
