from app.database.db import engine
from app.database.models import Base


def migrate():

    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    print("Database migration completed")


if __name__ == "__main__":
    migrate()