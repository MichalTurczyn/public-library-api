"""A repository for borrowing entity."""

from typing import Any
from datetime import date, datetime
from src.core.domain.borrowing import Borrowing, BorrowingIn
from src.core.repositories.iborrowing import IBorrowingRepository
from src.db import borrowing_table, database


class BorrowingRepository(IBorrowingRepository):
    """A class implementing the database borrowing repository."""

    async def create_borrowing(self, data: BorrowingIn) -> Any | None:
        """
        Creates a new borrowing record in the database.

        Args:
            data (BorrowingIn): The borrowing data to insert.

        Returns:
            Any | None: The newly created borrowing record if successful, otherwise None.
        """
        query = borrowing_table.insert().values(**data.model_dump())
        new_borrowing_id = await database.execute(query)
        return await self.get_borrowing_by_id(new_borrowing_id)

    async def get_borrowing_by_id(self, borrowing_id: int) -> Any | None:
        """
        Fetches a borrowing record by its ID.

        Args:
            borrowing_id (int): The ID of the borrowing.

        Returns:
            Any | None: The borrowing record if found, otherwise None.
        """
        query = borrowing_table.select().where(borrowing_table.c.id == borrowing_id)
        borrowing = await database.fetch_one(query)
        return Borrowing(**dict(borrowing)) if borrowing else None
    
    async def get_active_borrowings_by_user(self, user_id: int) -> list[Borrowing]:
        """Fetches active borrowings for a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list[Borrowing]: A list of active borrowings for the user.
        """
        query = borrowing_table.select().where(
            (borrowing_table.c.user_id == user_id) &
            (borrowing_table.c.status == "borrowed")
        )
        rows = await database.fetch_all(query)
        return [Borrowing(**row) for row in rows]

    async def list_all_borrowings(self) -> list[Borrowing]:
        """
        Retrieves all borrowing records from the database.

        Returns:
            list[Borrowing]: A list of all borrowing records.
        """
        query = borrowing_table.select()
        borrowings = await database.fetch_all(query)
        return [Borrowing(**dict(borrowing)) for borrowing in borrowings]
    
    async def mark_borrowing_as_returned(self, borrowing_id: int, return_date: date) -> bool:
        """Marks a borrowing as returned.

        Args:
            borrowing_id (int): ID of the borrowing to mark as returned.
            return_date (date): The actual return date.

        Returns:
            bool: True if the update was successful, otherwise False.
        """
        if self.get_borrowing_by_id(id):
            query = borrowing_table.update().where(borrowing_table.c.id == borrowing_id).values(
            status="returned",
            return_date=return_date)
            await database.execute(query)
            return True
        return False
    
    async def get_borrowing_history_by_user(self, user_id: int) -> list[Borrowing]:
        """Fetches the borrowing history for a specific user.

        Args:
            user_id (int): ID of the user.

        Returns:
            list[Borrowing]: List of borrowings with status 'returned'.
        """
        query = borrowing_table.select().where(
            (borrowing_table.c.user_id == user_id) &
            (borrowing_table.c.status == "returned")
        )
        rows = await database.fetch_all(query)
        return [Borrowing(**row) for row in rows]
    
    async def delete_borrowing(self, borrowing_id: int) -> bool:
        """Deletes a borrowing record by its id.

        Args:
            borrowing_id (int): ID of the borrowing to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        if self.get_borrowing_by_id(id):
            query = borrowing_table.delete().where(borrowing_table.c.id == borrowing_id)
            await database.execute(query)
            return True
        return False
    
    async def update_borrowing(self, borrowing_id: int, borrowing_data: BorrowingIn) -> Borrowing | None:
        """Updates an existing borrowing record.

        Args:
            borrowing_id (int): ID of the borrowing to update.
            borrowing_data (BorrowingIn): The updated borrowing data.

        Returns:
            Borrowing | None: The updated borrowing record if successful, otherwise None.
        """
        query = borrowing_table.update().where(borrowing_table.c.id == borrowing_id).values(
            **borrowing_data.model_dump()
        )
        result = await database.execute(query)
        if result:
            return await self.get_borrowing_by_id(borrowing_id)
        return None