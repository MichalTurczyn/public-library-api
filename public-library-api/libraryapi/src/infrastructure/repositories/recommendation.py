from typing import Any, List
from sqlalchemy import func, select
from src.core.domain.recommendation import Recommendation
from src.core.repositories.irecommendation import IRecommendationRepository
from src.db import book_table, database, borrowing_table, category_table


class RecommendationRepository(IRecommendationRepository):
    """A class implementing the database recommendation repository."""

    async def recommend_by_category(self, user_id: int) -> Recommendation:
        """
        Generates book recommendations based on the borrowing history by category.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Recommendation: Recommendations generated for the user based on categories.
        """
        # Query to get the most borrowed category by the user
        query = (
            select(category_table.c.id, func.count(borrowing_table.c.id).label("count"))
            .join(book_table, borrowing_table.c.book_id == book_table.c.id)
            .join(category_table, book_table.c.category_id == category_table.c.id)
            .where(borrowing_table.c.user_id == user_id)
            .group_by(category_table.c.id)
            .order_by(func.count(borrowing_table.c.id).desc())
        )
        result = await database.fetch_one(query)

        if not result:
            return Recommendation(user_id=user_id, recommended_books=[], reason="No borrowing history available.")

        # Fetch books in the recommended category
        category_id = result["id"]
        books_query = book_table.select().where(book_table.c.category_id == category_id)
        books = await database.fetch_all(books_query)

        recommended_books = [book["id"] for book in books]
        return Recommendation(user_id=user_id, recommended_books=recommended_books, reason="Based on your favorite category.")

    async def recommend_by_author(self, user_id: int) -> Recommendation:
        """
        Generates book recommendations based on the borrowing history by author.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Recommendation: Recommendations generated for the user based on authors.
        """
        # Query to get the most borrowed author by the user
        query = (
            select(book_table.c.author_id, func.count(borrowing_table.c.id).label("count"))
            .join(book_table, borrowing_table.c.book_id == book_table.c.id)
            .where(borrowing_table.c.user_id == user_id)
            .group_by(book_table.c.author_id)
            .order_by(func.count(borrowing_table.c.id).desc())
        )
        result = await database.fetch_one(query)

        if not result:
            return Recommendation(user_id=user_id, recommended_books=[], reason="No borrowing history available.")

        # Fetch books by the recommended author
        author_id = result["author_id"]
        books_query = book_table.select().where(book_table.c.author_id == author_id)
        books = await database.fetch_all(books_query)

        recommended_books = [book["id"] for book in books]
        return Recommendation(user_id=user_id, recommended_books=recommended_books, reason="Based on your favorite author.")
