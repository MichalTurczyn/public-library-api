from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide
from src.container import Container

from src.core.domain.author import Author, AuthorIn
from src.infrastructure.services.iauthor import IAuthorService
from src.infrastructure.dto.authordto import AuthorDTO

router = APIRouter(prefix="/Author", tags=["Author"])


@router.post("/", response_model=Author, status_code=201)
@inject
async def add_author(
    author: AuthorIn,
    service: IAuthorService = Depends(Provide[Container.author_service]),
) -> Author:
    """
    Adds a new author.

    Args:
        author (Author): New author data.
        service (IAuthorService): Service handling author operations.

    Returns:
        Author: Returns the created author.
    """
    return await service.add_author(author)


@router.get("/{author_id}", response_model=Author, status_code=200)
@inject
async def get_author_by_id(
    author_id: int,
    service: IAuthorService = Depends(Provide[Container.author_service]),
) -> Author:
    """
    Gets author data based on its id.

    Args:
        author_id (int): author id.
        service (IAuthorService): Service handling author operations.

    Raises:
        HTTPException: 404 if the author does not exist.

    Returns:
        Author: Author data.
    """
    author = await service.get_author_by_id(author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")
    return author


@router.get("/{author_id}/books", response_model=List[dict], status_code=200)
@inject
async def get_books_by_author(
    author_id: int,
    service: IAuthorService = Depends(Provide[Container.author_service]),
) -> List[dict]:
    """
    Gets a list of books written by a specific author.

    Args:
        author_id (int): author id.
        service (IAuthorService): Service handling author operations.

    Raises:
        HTTPException: 404 if the author has no books.

    Returns:
        List[dict]: List of books by the author.

    """
    books = await service.get_books_by_author(author_id)
    if not books:
        raise HTTPException(status_code=404, detail="No books found for this author.")
    return books


@router.get("/", response_model=List[Author], status_code=200)
@inject
async def list_authors(
    service: IAuthorService = Depends(Provide[Container.author_service]),
) -> List[Author]:
    """
    Returns a list of all authors.

    Args:
        service (IAuthorService): A service that handles author operations.

    Returns:
        List[Author]: A list of all authors.
    """
    return await service.list_authors()

@router.put("/{author_id}", response_model=AuthorDTO, status_code=200)
@inject
async def update_author(
    author_id: int,
    updated_data: AuthorIn,
    service: IAuthorService = Depends(Provide[Container.author_service]),
) -> Author:
    """
    Updates the data of an existing author.

    Args:
        author_id (int): Author id to update.
        updated_data (AuthorIn): Updated author data.
        service (IAuthorService): Service handling author operations.

    Raises:
        HTTPException: 404 if the author does not exist.

    Returns:
        Author: Updated author data.
    """
    author = await service.update_author(author_id, updated_data)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")
    return author

@router.delete("/{author_id}", status_code=200)
@inject
async def delete_author(
        author_id: int,
        service: IAuthorService = Depends(Provide[Container.author_service]),
):
    """
    Endpoint to delete an author by id.

    Args:
        author_id (int): id of the author.
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