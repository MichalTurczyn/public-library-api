"""Main module of the LibraryAPI app."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import http_exception_handler
from src.container import Container
from src.db import database, init_db

from src.api.routers.user import router as user_router
from src.api.routers.author import router as author_router
from src.api.routers.book import router as book_router
from src.api.routers.category import router as category_router
from src.api.routers.borrowing import router as borrowing_router
from src.api.routers.recommendation import router as recommendation_router



container = Container()
container.wire(modules=[
    "src.api.routers.user",
    "src.api.routers.author",
    "src.api.routers.book",
    "src.api.routers.category",
    "src.api.routers.borrowing",
    "src.api.routers.recommendation"
])


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    """Lifespan function working on app startup."""
    await init_db()
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/users")
app.include_router(author_router, prefix="/authors")
app.include_router(book_router, prefix="/books")
app.include_router(category_router, prefix="/categories")
app.include_router(borrowing_router, prefix="/borrowings")
app.include_router(recommendation_router, prefix="/recommendations")
@app.get("/")
async def root():
    return {"message": "Welcome to LibraryAPI"}

@app.exception_handler(HTTPException)
async def http_exception_handle_logging(
    request: Request,
    exception: HTTPException,
) -> Response:
    """A function handling http exceptions for logging purposes.

    Args:
        request (Request): The incoming HTTP request.
        exception (HTTPException): A related exception.

    Returns:
        Response: The HTTP response.
    """
    return await http_exception_handler(request, exception)
