
from typing import Any
from pydantic import UUID4
from src.core.domain.author import Author, AuthorIn
from src.core.repositories.iauthor import IAuthorRepository
from src.db import author_table, database


class AuthorRepository(IAuthorRepository):

    async def add_author(self, data: AuthorIn) -> Any | None:
        query = author_table.insert().values(**data.model_dump())
        new_author_id = await database.execute(query)
        return await self.get_by_uuid(new_author_id)

    async def get_author_by_uuid(self, author_id: UUID4) -> Any | None:
        query = author_table.select().where(author_table.c.id == author_id)
        author = await database.fetch_one(query)
        return Author(**dict(author)) if author else None

    async def delete_author(self, author_id: UUID4) -> bool:
        query = author_table.delete().where(author_table.c.id == author_id)
        result = await database.execute(query)
        return result > 0

    async def list_authors(self) -> list[Author]:
        query = author_table.select()
        authors = await database.fetch_all(query)
        return [Author(**dict(author)) for author in authors]
