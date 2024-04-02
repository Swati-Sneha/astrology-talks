from typing import Any, Union

from app.database.base import BaseCrud
from app.database.models.users import User


class Users(BaseCrud):  # type: ignore
    """Handle DB operations upon users collection."""

    _model_class = User
    _collection_name: str = "users"

    async def get_user_by_email(self, email: str) -> Union[User, None]:
        """Return user from the DB."""
        user = await self._collection.find_one({"emailId": email}, {"_id": 0})

        if user:
            user["dob"] = user["dob"].isoformat()
            return user

        return None

    async def register_user(self, user: User) -> None:
        """Insert user into the DB."""
        user_obj = user.dict()

        await self._collection.insert_one(user_obj)


users_db = Users()
