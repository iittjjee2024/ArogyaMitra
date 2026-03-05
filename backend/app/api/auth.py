from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.db import SessionLocal
from ..database import models, schemas
from ..core.security import hash_password, verify_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    yield db
    db.close()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed = hash_password(user.password)

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed,
        age=user.age,
        weight=user.weight,
        height=user.height,
        goal=user.goal
    )

    db.add(new_user)
    db.commit()

    return {"message":"User created"}