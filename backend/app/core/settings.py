from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    PROJECT_NAME: str = "ArogyaMitra"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str = "sqlite:///./arogya_mitra.db"

    GROQ_API_KEY: Optional[str] = None
    GROQ_MODEL: str = "llama3-8b-8192"
    BACKEND_CORS_ORIGINS: list = ["*"]


    STATIC_DIR: str = "static"
    IMAGE_DIR: str = "static/images"
    REPORT_DIR: str = "static/reports"

    MAX_WORKOUT_DAYS: int = 7
    MAX_MEAL_DAYS: int = 7


    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()