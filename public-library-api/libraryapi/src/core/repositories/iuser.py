"""A repository for user entity."""

from abc import ABC, abstractmethod
from typing import Any
from pydantic import UUID4
from src.core.domain.user import UserIn


class IUserRepository(ABC):
    """An abstract repository class for user."""

    @abstractmethod
    async def register_user(self, user: UserIn) -> Any | None:
        """A method registering new user.

        Args:
            user (UserIn): The user input data.

        Returns:
            Any | None: The new user object.
        """
        pass

    @abstractmethod
    async def get_by_uuid(self, uuid: UUID4) -> Any | None:
        """A method getting user by UUID.

        Args:
            uuid (UUID5): UUID of the user.

        Returns:
            Any | None: The user object if exists.
        """
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Any | None:
        """A method getting user by email.

        Args:
            email (str): The email of the user.

        Returns:
            Any | None: The user object if exists.
        """
        pass

    @abstractmethod
    async def update_user(self, uuid: UUID4, user_data: UserIn) -> Any | None:
        """A method updating user information.

        Args:
            uuid (UUID5): UUID of the user to update.
            user_data (UserIn): The updated user data.

        Returns:
            Any | None: The updated user object if the operation was successful.
        """
        pass

    @abstractmethod
    async def delete_user(self, uuid: UUID4) -> bool:
        """A method deleting a user by UUID.

        Args:
            uuid (UUID5): UUID of the user to delete.

        Returns:
            bool: True if the user was successfully deleted, False otherwise.
        """
        pass
