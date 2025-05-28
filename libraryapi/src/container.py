"""Module providing containers injecting dependencies for LibraryAPI."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from src.infrastructure.repositories.user import UserRepository
from src.infrastructure.services.user import UserService
from src.infrastructure.repositories.book import BookRepository
from src.infrastructure.services.book import BookService
from src.infrastructure.repositories.author import AuthorRepository
from src.infrastructure.services.author import AuthorService
from src.infrastructure.repositories.category import CategoryRepository
from src.infrastructure.services.category import CategoryService
from src.infrastructure.repositories.borrowing import BorrowingRepository
from src.infrastructure.services.borrowing import BorrowingService
from src.infrastructure.repositories.recommendation import RecommendationRepository
from src.infrastructure.services.recommendation import RecommendationService



class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""

    # Repositories

    user_repository = Singleton(UserRepository)
    book_repository = Singleton(BookRepository)
    author_repository = Singleton(AuthorRepository)
    category_repository = Singleton(CategoryRepository)
    borrowing_repository = Singleton(BorrowingRepository)
    recommendation_repository = Singleton(RecommendationRepository)

    # Services
    user_service = Factory(
        UserService,
        repository=user_repository,
    )
    book_service = Factory(
        BookService,
        repository=book_repository,
    )
    author_service = Factory(
        AuthorService,
        repository=author_repository,
    )
    category_service = Factory(
        CategoryService,
        repository=category_repository,
    )
    borrowing_service = Factory(
        BorrowingService,
        repository=borrowing_repository,
    )
    recommendation_service = Factory(
        RecommendationService,
        repository=recommendation_repository,
    )
