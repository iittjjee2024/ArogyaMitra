from sqlalchemy import Column, Integer, String, Float
from .db import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    goal = Column(String)