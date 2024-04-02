import pydantic
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MONGO_URI: str = Field(
        default="mongodb://localhost:27017/",
        description="Full mongo DSN (https://www.mongodb.com/docs/manual/reference/connection-string/).",
    )
    DATABASE_NAME: str = Field(
        default="astrologer", description="database name in MongoDB."
    )

    JWT_SECRET: str = Field(default="", description="JWT secret key")
    OPEN_AI_KEY: str = Field(default="", description="OpenAI API key")
    PORT: int = Field(default=4000, description="Port to run the server on")


settings = Settings()
