from typing import Any
from pydantic import UUID4
from src.core.domain.book import Book, BookIn
from src.core.repositories.ibook import IBookRepository
from src.db import book_table, database


class BookRepository(IBookRepository):

    async def get_book_by_uuid(self, book_id: UUID4) -> Any | None:
        query = book_table.select().where(book_table.c.book_id == book_id)
        book = await database.fetch_one(query)
        return Book(**dict(book)) if book else None

    async def add_book(self, data: BookIn) -> Any | None:
        query = book_table.insert().values(**data.model_dump())
        new_book_id = await database.execute(query)
        return await self.get_book_by_uuid(new_book_id)

    async def update_book(self, book_id: UUID4, data: BookIn) -> Any | None:
        query = book_table.update().where(book_table.c.book_id == book_id).values(**data.model_dump())
        await database.execute(query)
        return await self.get_book_by_uuid(book_id)

    async def delete_book(self, book_id: UUID4) -> bool:
        query = book_table.delete().where(book_table.c.book_id == book_id)
        result = await database.execute(query)
        return result > 0

    async def list_books(self) -> list[Book]:
        query = book_table.select()
        books = await database.fetch_all(query)
        return [Book(**dict(book)) for book in books]

    async def search_book_by_title(self, title: str) -> Any:
        query = book_table.select().where(book_table.c.title.ilike(f"%{title}%"))
        rows = await database.fetch_all(query)
        return [Book(**row) for row in rows]

    async def search_book_by_author(self, author_id: UUID4) -> Any:
        query = book_table.select().where(book_table.c.author_id == author_id)
        rows = await database.fetch_all(query)
        return [Book(**row) for row in rows]

    async def search_book_by_category(self, category_id: UUID4) -> Any:
        query = book_table.select().where(book_table.c.category_id == category_id)
        rows = await database.fetch_all(query)
        return [Book(**row) for row in rows]