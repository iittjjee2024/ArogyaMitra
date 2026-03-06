from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):

    db_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password,
        age=user.age,
        weight=user.weight,
        height=user.height
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(db: Session, email: str):

    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(db: Session, user_id: int):

    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user_data: dict):

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        return None

    for key, value in user_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user

def create_workout(db: Session, workout: schemas.WorkoutCreate):

    db_workout = models.Workout(
        user_id=workout.user_id,
        name=workout.name,
        duration=workout.duration,
        calories_burned=workout.calories_burned
    )

    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)

    return db_workout


def get_user_workouts(db: Session, user_id: int):

    return db.query(models.Workout).filter(models.Workout.user_id == user_id).all()

def create_nutrition(db: Session, nutrition: schemas.NutritionCreate):

    db_nutrition = models.Nutrition(
        user_id=nutrition.user_id,
        meal=nutrition.meal,
        calories=nutrition.calories,
        protein=nutrition.protein,
        carbs=nutrition.carbs,
        fats=nutrition.fats
    )

    db.add(db_nutrition)
    db.commit()
    db.refresh(db_nutrition)

    return db_nutrition


def get_user_nutrition(db: Session, user_id: int):

    return db.query(models.Nutrition).filter(models.Nutrition.user_id == user_id).all()


def create_health_record(db: Session, record: schemas.HealthCreate):

    db_record = models.HealthRecord(
        user_id=record.user_id,
        bmi=record.bmi,
        heart_rate=record.heart_rate,
        blood_pressure=record.blood_pressure
    )

    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return db_record


def get_health_records(db: Session, user_id: int):

    return db.query(models.HealthRecord).filter(models.HealthRecord.user_id == user_id).all()