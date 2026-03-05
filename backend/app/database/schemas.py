from pydantic import BaseModel

class UserCreate(BaseModel):

    name: str
    email: str
    password: str
    age: int
    weight: float
    height: float
    goal: str


class Login(BaseModel):

    email: str
    password: str


class ChatRequest(BaseModel):

    message: str