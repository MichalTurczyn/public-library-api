"""Module providing containers injecting dependencies for LibraryAPI."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from src.infrastructure.repositories.author import AuthorRepository
from src.infrastructure.repositories.book import BookRepository
from src.infrastructure.repositories.category import CategoryRepository
from src.infrastructure.repositories.borrowing import BorrowingRepository
from src.infrastructure.repositories.fine import FineRepository
from src.infrastructure.repositories.user import UserRepository
from src.infrastructure.repositories.recommendation import RecommendationRepository
from src.infrastructure.repositories.reservation import ReservationRepository
from src.infrastructure.services.author import AuthorService
from src.infrastructure.services.book import BookService
from src.infrastructure.services.category import CategoryService
from src.infrastructure.services.borrowing import BorrowingService
from src.infrastructure.services.fine import FineService
from src.infrastructure.services.user import UserService
from src.infrastructure.services.recommendation import RecommendationService
from src.infrastructure.services.reservation import ReservationService


class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""

    # Repositories
    author_repository = Singleton(AuthorRepository)
    book_repository = Singleton(BookRepository)
    category_repository = Singleton(CategoryRepository)
    borrowing_repository = Singleton(BorrowingRepository)
    fine_repository = Singleton(FineRepository)
    user_repository = Singleton(UserRepository)
    recommendation_repository = Singleton(RecommendationRepository)
    reservation_repository = Singleton(ReservationRepository)

    # Services
    author_service = Factory(
        AuthorService,
        repository=author_repository,
    )
    book_service = Factory(
        BookService,
        repository=book_repository,
    )
    category_service = Factory(
        CategoryService,
        repository=category_repository,
    )
    borrowing_service = Factory(
        BorrowingService,
        repository=borrowing_repository,
    )
    fine_service = Factory(
        FineService,
        repository=fine_repository,
    )
    user_service = Factory(
        UserService,
        repository=user_repository,
    )
    recommendation_service = Factory(
        RecommendationService,
        repository=recommendation_repository,
    )
    reservation_service = Factory(
        ReservationService,
        repository=reservation_repository,
    )
