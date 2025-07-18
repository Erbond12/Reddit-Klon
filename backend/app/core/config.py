from pathlib import Path
from typing import Set

from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    NEO4J_BOLT_URL: str
    NEO4J_TEST_BOLT_URL: str
    MONGODB_URI: str
    MONGODB_TEST_URI: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    SUB_PREFIX: str = "uid:"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    REDIS_DSN: RedisDsn

    MAX_TITLE_LENGTH = 300
    MAX_USERNAME_LENGTH = 20
    MAX_SR_LENGTH = 21
    MAX_DESCRIPTION_LENGTH = 500

    MIN_USERNAME_LENGTH = 3
    MIN_SR_LENGTH = 3

    TEST_USER_USERNAME: str
    TEST_USER_EMAIL: str
    TEST_USER_PASSWORD: str

    AZURE_STORAGE_CREDENTIALS: str

    FRONTEND_ORIGINS: Set[str] = {
        "http://localhost:3000",
        # removed
    }

    class Config:
        case_sensitive = True
        env_file = Path(__file__).parent.parent.absolute() / Path(".env")


settings = Settings()
