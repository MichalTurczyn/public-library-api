"""A repository for user entity."""


from typing import Any
from src.infrastructure.utils.password import hash_password
from src.core.domain.user import UserIn, User
from src.core.repositories.iuser import IUserRepository
from src.db import database, user_table


class UserRepository(IUserRepository):
    """An implementation of repository class for user."""

    async def register_user(self, user: UserIn) -> Any | None:
        """A method registering new user.

        Args:
            user (UserIn): The user input data.

        Returns:
            Any | None: The new user object.
        """

        if await self.get_user_by_email(user.email):
            return None

        user.password = hash_password(user.password)

        query = user_table.insert().values(**user.model_dump())
        new_user_id = await database.execute(query)

        return await self.get_user_by_id(new_user_id)
    

        token_details = TokenDTO(
            token_type="Bearer",
            user_token="mock_token_12345",
            expires=datetime.utcnow() + timedelta(hours=1)
        )
        return token_details
    
    async def list_users(self) -> list[User]:
        """
        Lists all users.

        Returns:
            list[User]: A list of all user objects.
        """
        query = user_table.select()
        users = await database.fetch_all(query)
        return [User(**dict(user)) for user in users]

    async def get_user_by_id(self, id: int) -> Any | None:
        """A method getting user by id.

        Args:
            id (id5): id of the user.

        Returns:
            Any | None: The user object if exists.
        """

        query = user_table \
            .select() \
            .where(user_table.c.id == id)
        user = await database.fetch_one(query)

        return user

    async def get_user_by_email(self, email: str) -> Any | None:
        """A method getting user by email.

        Args:
            email (str): The email of the user.

        Returns:
            Any | None: The user object if exists.
        """

        query = user_table \
            .select() \
            .where(user_table.c.email == email)
        user = await database.fetch_one(query)

        return user
    
    async def update_user(self, id: int, user_data: UserIn) -> User | None:
        """
        Updates a user's data.

        Args:
            id (int): The ID of the user to update.
            user_data (UserIn): The updated user data.

        Returns:
            User | None: The updated user object if successful, otherwise None.
        """
        query = user_table.update().where(user_table.c.id == id).values(**user_data.dict())
        await database.execute(query)

        return await self.get_user_by_id(id)

    async def delete_user(self, id: int) -> bool:
        """
        Deletes a user by their ID.

        Args:
            id (int): The ID of the user to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        if self.get_user_by_id(id):
            query = user_table.delete().where(user_table.c.id == id)
            await database.execute(query)
            return True

        return False