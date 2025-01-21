"""A module providing database access."""

import asyncio

import databases
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import OperationalError, DatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from asyncpg.exceptions import (
    CannotConnectNowError,
    ConnectionDoesNotExistError,
)
from src.config import config as settings


metadata = sqlalchemy.MetaData()

# Users table
user_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("gen_random_uuid()"),
    ),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, nullable=False),
    sqlalchemy.Column("password", sqlalchemy.String, nullable=False),
)

# Authors table
author_table = sqlalchemy.Table(
    "authors",
    metadata,
    sqlalchemy.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("gen_random_uuid()"),
    ),
    sqlalchemy.Column("first_name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("last_name", sqlalchemy.String, nullable=False),
)

# Books table
book_table = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column(
        "book_id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("gen_random_uuid()"),
    ),
    sqlalchemy.Column("title", sqlalchemy.String, nullable=False),
    sqlalchemy.Column(
        "author_id",
        sqlalchemy.ForeignKey("authors.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sqlalchemy.Column("published_year", sqlalchemy.Integer, nullable=True),
    # Dodanie kolumny category_id, która będzie odnosiła się do tabeli categories
    sqlalchemy.Column(
        "category_id",
        sqlalchemy.ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False,
    ),
)

# Categories table
category_table = sqlalchemy.Table(
    "categories",
    metadata,
    sqlalchemy.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("gen_random_uuid()"),
    ),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
)

# Borrowings table
borrowing_table = sqlalchemy.Table(
    "borrowings",
    metadata,
    sqlalchemy.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("gen_random_uuid()"),
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
    sqlalchemy.Column("return_date", sqlalchemy.Date, nullable=True),
    sqlalchemy.Column("returned_date", sqlalchemy.DateTime, nullable=True),
)

# Fines table
fine_table = sqlalchemy.Table(
    "fines",
    metadata,
    sqlalchemy.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("gen_random_uuid()"),
    ),
    sqlalchemy.Column(
        "user_id",
        sqlalchemy.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sqlalchemy.Column(
        "borrowing_id",
        sqlalchemy.ForeignKey("borrowings.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sqlalchemy.Column("amount", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.text("now()")),
)

# Recommendations table
recommendation_table = sqlalchemy.Table(
    "recommendations",
    metadata,
    sqlalchemy.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("gen_random_uuid()"),
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
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.text("now()")),
)

reservation_table = sqlalchemy.Table(
    "reservations",
    metadata,
    sqlalchemy.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("gen_random_uuid()"),
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
    sqlalchemy.Column("status", sqlalchemy.String, nullable=False, default="active"),
    sqlalchemy.Column("reserved_at", sqlalchemy.DateTime, server_default=sqlalchemy.text("now()")),
)

# Database URI
engine = create_async_engine(
    settings.DB_URI,
    echo=settings.DEBUG,
    future=True,
    pool_pre_ping=True,
)

database = databases.Database(
    settings.DB_URI,
    force_rollback=settings.DEBUG,
)


async def init_db(retries: int = 5, delay: int = 5) -> None:
    """Function initializing the DB.

    Args:
        retries (int, optional): Number of retries to connect to DB. Defaults to 5.
        delay (int, optional): Delay between connection retries. Defaults to 5.
    """
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(metadata.create_all)
            print("Database initialized successfully.")
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
