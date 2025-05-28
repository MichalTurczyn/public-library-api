from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status
from src.container import Container
from typing import List

from src.core.domain.book import Book, BookIn
from src.infrastructure.services.ibook import IBookService
from src.infrastructure.dto.bookdto import BookDTO

router = APIRouter(prefix="/Book", tags=["Book"])


@router.post("/", response_model=BookDTO, status_code=201)
@inject
async def add_book(
    book: BookIn,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> Book:
    """
    Endpoint for adding a new book.

    Args:
        book (BookIn): The book data to add.
        service (IBookService): The injected book service dependency.

    Returns:
        Book: The newly added book.
    """
    new_book = await service.add_book(book)
    if new_book:
        return new_book
    raise HTTPException(status_code=400, detail="Unable to create book")


@router.get("/", response_model=List[BookDTO], status_code=200)
@inject
async def list_books(
    service: IBookService = Depends(Provide[Container.book_service]),
) -> List[BookDTO]:
    """
    Endpoint to get list of all books.

    Args:
        service (IBookService): Injected dependency of book service.

    Returns:
        list[Book]: List of books.
    """
    return await service.list_books()


@router.get("/{book_id}", response_model=BookDTO, status_code=200)
@inject
async def get_book_by_id(
    book_id: int,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> Book:
    """
    Endpoint to fetch a book based on its id.

    Args:
        book_id (int): The book's id.
        service (IBookService): The injected book service dependency.

    Raises:
        HTTPException: 404 if the book doesn't exist.

    Returns:
        Book: The book details.
    """
    book = await service.get_book_by_id(book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.get("/search/title/{title}", response_model=list[Book], status_code=200)
@inject
async def search_book_by_title(
    title: str,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> list[Book]:
    """
    Endpoint for searching for books by title.

    Args:
        title (str): Title of the book.
        service (IBookService): Injected dependency of the book service.

    Returns:
        list[Book]: List of books that match the title.
    """
    books = await service.search_book_by_title(title)
    if books:
        return books
    raise HTTPException(status_code=404, detail="No books found with this title")

@router.get("/search/author/{author_id}", response_model=list[Book], status_code=200)
@inject
async def search_book_by_author(
    author_id: int,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> list[Book]:
    """
    Endpoint for searching books by author.

    Args:
        author_id (int): The author id of the book.
        service (IBookService): Injected dependency of the book service.

    Returns:
        list[Book]: List of books written by the author.
    """
    books = await service.search_book_by_author(author_id)
    if books:
        return books
    raise HTTPException(status_code=404, detail="No books found for this author")

@router.get("/search/category/{category_id}", response_model=list[Book], status_code=200)
@inject
async def search_book_by_category(
    category_id: int,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> list[Book]:
    """
    Endpoint for searching books by category.

    Args:
        category_id (int): the book's category id.
        service (IBookService): Injected book service dependency.

    Returns:
        list[Book]: List of books belonging to the category.

    """
    books = await service.search_book_by_category(category_id)
    if books:
        return books
    raise HTTPException(status_code=404, detail="No books found for this category")

@router.put("/{book_id}", response_model=BookDTO, status_code=200)
@inject
async def update_book(
    book_id: int,
    updated_data: BookIn,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> Book:
    """
    Endpoint for updating book data.

    Args:
        book_id (int): Book ID.
        updated_data (BookIn): Updated book data.
        service (IBookService): Injected book service dependency.

    Raises:
        HTTPException: 404 if book does not exist.

    Returns:
        Book: Updated book.
    """
    updated_book = await service.update_book(book_id, updated_data)
    if updated_book:
        return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/{book_id}", status_code=204)
@inject
async def delete_book(
    book_id: int,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> None:
    """
    Endpoint to delete a book based on its id.

    Args:
        book_id (int): The book's id.
        service (IBookService): The injected book service dependency.

    Raises:
        HTTPException: 404 if the book does not exist.
    """
    result = await service.delete_book(book_id)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")