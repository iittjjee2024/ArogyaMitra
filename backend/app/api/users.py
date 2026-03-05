from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import models, schemas
from ..database.db import SessionLocal

router = APIRouter()


def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create_user")

def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user