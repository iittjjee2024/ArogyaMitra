import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    PROJECT_NAME = "ArogyaMitra"

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./arogya_mitra.db"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "super-secret-key"
    )

    ALGORITHM = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES = 60


settings = Settings()
