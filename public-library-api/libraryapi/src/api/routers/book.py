from pydantic import UUID4
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status
from src.container import Container
from src.core.domain.book import Book, BookIn
from src.infrastructure.services.ibook import IBookService

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
@inject
async def add_book(
    book: BookIn,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> Book:
    """
    Endpoint do dodawania nowej książki.

    Args:
        book (BookIn): Dane książki do dodania.
        service (IBookService): Wstrzyknięta zależność serwisu książek.

    Returns:
        Book: Nowo dodana książka.
    """
    new_book = await service.add_book(book)
    if new_book:
        return new_book
    raise HTTPException(status_code=400, detail="Unable to create book")


@router.get("/", response_model=list[Book], status_code=status.HTTP_200_OK)
@inject
async def list_books(
    service: IBookService = Depends(Provide[Container.book_service]),
) -> list[Book]:
    """
    Endpoint do pobierania listy wszystkich książek.

    Args:
        service (IBookService): Wstrzyknięta zależność serwisu książek.

    Returns:
        list[Book]: Lista książek.
    """
    return await service.list_books()


@router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
@inject
async def get_book_by_uuid(
    book_id: UUID4,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> Book:
    """
    Endpoint do pobierania książki na podstawie identyfikatora UUID.

    Args:
        book_id (UUID): Identyfikator książki.
        service (IBookService): Wstrzyknięta zależność serwisu książek.

    Raises:
        HTTPException: 404 jeśli książka nie istnieje.

    Returns:
        Book: Szczegóły książki.
    """
    book = await service.get_book_by_uuid(book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
@inject
async def update_book(
    book_id: UUID4,
    updated_data: BookIn,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> Book:
    """
    Endpoint do aktualizacji danych książki.

    Args:
        book_id (UUID): Identyfikator książki.
        updated_data (BookIn): Zaktualizowane dane książki.
        service (IBookService): Wstrzyknięta zależność serwisu książek.

    Raises:
        HTTPException: 404 jeśli książka nie istnieje.

    Returns:
        Book: Zaktualizowana książka.
    """
    updated_book = await service.update_book(book_id, updated_data)
    if updated_book:
        return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_book(
    book_id: UUID4,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> None:
    """
    Endpoint do usuwania książki na podstawie identyfikatora UUID.

    Args:
        book_id (UUID): Identyfikator książki.
        service (IBookService): Wstrzyknięta zależność serwisu książek.

    Raises:
        HTTPException: 404 jeśli książka nie istnieje.
    """
    result = await service.delete_book(book_id)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")


@router.get("/search/title/{title}", response_model=list[Book], status_code=status.HTTP_200_OK)
@inject
async def search_book_by_title(
    title: str,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> list[Book]:
    """
    Endpoint do wyszukiwania książek po tytule.

    Args:
        title (str): Tytuł książki.
        service (IBookService): Wstrzyknięta zależność serwisu książek.

    Returns:
        list[Book]: Lista książek, które pasują do tytułu.
    """
    books = await service.search_book_by_title(title)
    if books:
        return books
    raise HTTPException(status_code=404, detail="No books found with this title")

@router.get("/search/author/{author_id}", response_model=list[Book], status_code=status.HTTP_200_OK)
@inject
async def search_book_by_author(
    author_id: UUID4,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> list[Book]:
    """
    Endpoint do wyszukiwania książek po autorze.

    Args:
        author_id (UUID4): UUID autora książki.
        service (IBookService): Wstrzyknięta zależność serwisu książek.

    Returns:
        list[Book]: Lista książek napisanych przez autora.
    """
    books = await service.search_book_by_author(author_id)
    if books:
        return books
    raise HTTPException(status_code=404, detail="No books found for this author")

@router.get("/search/category/{category_id}", response_model=list[Book], status_code=status.HTTP_200_OK)
@inject
async def search_book_by_category(
    category_id: UUID4,
    service: IBookService = Depends(Provide[Container.book_service]),
) -> list[Book]:
    """
    Endpoint do wyszukiwania książek po kategorii.

    Args:
        category_id (UUID4): UUID kategorii książki.
        service (IBookService): Wstrzyknięta zależność serwisu książek.

    Returns:
        list[Book]: Lista książek należących do kategorii.
    """
    books = await service.search_book_by_category(category_id)
    if books:
        return books
    raise HTTPException(status_code=404, detail="No books found for this category")