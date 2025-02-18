"""A module providing database access."""

import asyncio

import databases
import sqlalchemy
from sqlalchemy.exc import OperationalError, DatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.mutable import MutableList
from asyncpg.exceptions import (
    CannotConnectNowError,
    ConnectionDoesNotExistError,
)
from src.config import config


metadata = sqlalchemy.MetaData()

# Users table
user_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column(
        "id",
        sqlalchemy.Integer,
        primary_key=True,
    ),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, nullable=False),
    sqlalchemy.Column("password", sqlalchemy.String, nullable=False),
)


# Books table
book_table = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column(
        "id",
        sqlalchemy.Integer,
        primary_key=True,
    ),
    sqlalchemy.Column("title", sqlalchemy.String, nullable=False),
    sqlalchemy.Column(
        "author_id",
        sqlalchemy.ForeignKey("authors.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sqlalchemy.Column("published_year", sqlalchemy.Integer, nullable=True),
    sqlalchemy.Column("isbn", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("copies_available", sqlalchemy.Integer, nullable=True),
    sqlalchemy.Column(
        "category_id",
        sqlalchemy.ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False,
    ),
)


# Authors table
author_table = sqlalchemy.Table(
    "authors",
    metadata,
    sqlalchemy.Column(
        "id",
        sqlalchemy.Integer,
        primary_key=True,
    ),
    sqlalchemy.Column("first_name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("last_name", sqlalchemy.String, nullable=False),
)


# Categories table
category_table = sqlalchemy.Table(
    "categories",
    metadata,
    sqlalchemy.Column(
        "id",
        sqlalchemy.Integer,
        primary_key=True,
    ),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=False),
)


# Borrowings table
borrowing_table = sqlalchemy.Table(
    "borrowings",
    metadata,
    sqlalchemy.Column(
        "id",
        sqlalchemy.Integer,
        primary_key=True,
    ),
    sqlalchemy.Column(
        "user_id",
        sqlalchemy.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sqlalchemy.Column(
        "book_id",
        sqlalchemy.ForeignKey("books.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sqlalchemy.Column("borrowed_date", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("planned_return_date", sqlalchemy.Date, nullable=True),
    sqlalchemy.Column("return_date", sqlalchemy.Date, nullable=True),
    sqlalchemy.Column(
        "status",
        sqlalchemy.String,
        nullable=False,
        default="borrowed",
    ),
)



db_uri = (
    f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}/{config.DB_NAME}"
)

engine = create_async_engine(
    db_uri,
    echo=True,
    future=True,
    pool_pre_ping=True,
)

database = databases.Database(
    db_uri,
    force_rollback=True,
)


async def init_db(retries: int = 5, delay: int = 5) -> None:
    """Function initializing the DB.

    Args:
        retries (int, optional): Number of retries of connect to DB.
            Defaults to 5.
        delay (int, optional): Delay of connect do DB. Defaults to 2.
    """
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(metadata.create_all)
            return
        except (
            OperationalError,
            DatabaseError,
            CannotConnectNowError,
            ConnectionDoesNotExistError,
        ) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(delay)

    raise ConnectionError("Could not connect to DB after several retries.")

