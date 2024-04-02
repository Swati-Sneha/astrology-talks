from motor import motor_asyncio

from app.settings import settings
from app.utilities.singleton import SingletonMeta


class Database(metaclass=SingletonMeta):
    """Database Singleton Connector and configurator class."""

    def __init__(self) -> None:
        """Instance the db connection."""
        print(f"🟢 Connecting to MongoDB! {settings.MONGO_URI}")
        self.client = motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
        print(f"🟢 Connected to MongoDB! {settings.MONGO_URI}")
        self.db = self.client[settings.DATABASE_NAME]
        print(f"🟢 Selected DB: {settings.DATABASE_NAME}")
