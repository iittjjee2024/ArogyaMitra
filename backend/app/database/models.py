from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database.db import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)

class Workout(Base):

    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    workout_name = Column(String)
    duration = Column(Integer)

class Nutrition(Base):

    __tablename__ = "nutrition"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    meal = Column(String)
    calories = Column(Float)
    