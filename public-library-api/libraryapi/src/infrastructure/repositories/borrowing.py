"""A repository for borrowing entity."""

from typing import Any
from pydantic import UUID4
from datetime import datetime
from src.core.domain.borrowing import Borrowing, BorrowingIn
from src.core.repositories.iborrowing import IBorrowingRepository
from src.db import borrowing_table, database


class BorrowingRepository(IBorrowingRepository):
    """A class implementing the database borrowing repository."""

    async def borrow_book(self, data: BorrowingIn) -> Any | None:
        query = borrowing_table.insert().values(**data.model_dump())
        new_borrowing_id = await database.execute(query)
        return await self.get_book_by_uuid(new_borrowing_id)

    async def return_book(self, borrowing_id: UUID4) -> bool:
        query = borrowing_table.update().where(borrowing_table.c.id == borrowing_id).values(
            returned_date=datetime.utcnow()
        )
        result = await database.execute(query)
        return result > 0

    async def get_book_by_uuid(self, borrowing_id: UUID4) -> Any | None:
        query = borrowing_table.select().where(borrowing_table.c.id == borrowing_id)
        borrowing = await database.fetch_one(query)
        return Borrowing(**dict(borrowing)) if borrowing else None

    async def list_borrowings_by_user(self, user_id: UUID4) -> list[Borrowing]:
        query = borrowing_table.select().where(borrowing_table.c.user_id == user_id)
        borrowings = await database.fetch_all(query)
        return [Borrowing(**dict(borrowing)) for borrowing in borrowings]

    async def get_borrowing_history(self, user_id: UUID4) -> list[Borrowing]:
        query = borrowing_table.select().where(
            (borrowing_table.c.user_id == user_id) &
            (borrowing_table.c.returned_date.isnot(None))  # Only completed borrowings
        )
        rows = await database.fetch_all(query)
        return [Borrowing(**row) for row in rows]