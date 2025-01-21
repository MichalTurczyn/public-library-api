
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from pydantic import UUID4
from dependency_injector.wiring import inject, Provide
from src.container import Container
from src.core.domain.author import Author
from src.infrastructure.services.iauthor import IAuthorService

router = APIRouter(prefix="/authors", tags=["authors"])


@router.post("/", response_model=Author, status_code=status.HTTP_201_CREATED)
@inject
async def add_author(
    author: Author,
    service: IAuthorService = Depends(Provide[Container.author_service]),
) -> Author:
    """
    Dodaje nowego autora.

    Args:
        author (Author): Dane nowego autora.
        service (IAuthorService): Serwis obsługujący operacje na autorach.

    Returns:
        Author: Zwraca utworzonego autora.
    """
    return await service.add_author(author)


@router.get("/{author_id}", response_model=Author, status_code=status.HTTP_200_OK)
@inject
async def get_author_by_id(
    author_id: UUID4,
    service: IAuthorService = Depends(Provide[Container.author_service]),
) -> Author:
    """
    Pobiera dane autora na podstawie jego UUID.

    Args:
        author_id (UUID4): UUID autora.
        service (IAuthorService): Serwis obsługujący operacje na autorach.

    Raises:
        HTTPException: 404 jeśli autor nie istnieje.

    Returns:
        Author: Dane autora.
    """
    author = await service.get_author_by_id(author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")
    return author


@router.get("/{author_id}/books", response_model=List[dict], status_code=status.HTTP_200_OK)
@inject
async def get_books_by_author(
    author_id: UUID4,
    service: IAuthorService = Depends(Provide[Container.author_service]),
) -> List[dict]:
    """
    Pobiera listę książek napisanych przez konkretnego autora.

    Args:
        author_id (UUID4): UUID autora.
        service (IAuthorService): Serwis obsługujący operacje na autorach.

    Raises:
        HTTPException: 404 jeśli autor nie ma książek.

    Returns:
        List[dict]: Lista książek autora.
    """
    books = await service.get_books_by_author(author_id)
    if not books:
        raise HTTPException(status_code=404, detail="No books found for this author.")
    return books


@router.get("/", response_model=List[Author], status_code=status.HTTP_200_OK)
@inject
async def list_authors(
    service: IAuthorService = Depends(Provide[Container.author_service]),
) -> List[Author]:
    """
    Zwraca listę wszystkich autorów.

    Args:
        service (IAuthorService): Serwis obsługujący operacje na autorach.

    Returns:
        List[Author]: Lista wszystkich autorów.
    """
    return await service.list_authors()



@router.delete("/{author_id}", status_code=status.HTTP_200_OK)
@inject
async def delete_author(
        author_id: UUID4,
        service: IAuthorService = Depends(Provide[Container.author_service]),
):
    """
    Endpoint to delete an author by UUID.

    Args:
        author_id (UUID4): UUID of the author.
        service (IAuthorService): Injected author service.

    Raises:
        HTTPException: 404 if the author does not exist.

    Returns:
        dict: Success message.
    """
    success = await service.delete_author(author_id)
    if not success:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}