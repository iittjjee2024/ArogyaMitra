from fastapi import FastAPI
from .api import users, workout, nutrition, coach
from .database.db import engine
from .database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ArogyaMitra AI Health System"
)

app.include_router(users.router, prefix="/users")
app.include_router(workout.router, prefix="/workout")
app.include_router(nutrition.router, prefix="/nutrition")
app.include_router(coach.router, prefix="/coach")


@app.get("/")
def home():

    return {
        "message": "ArogyaMitra AI Backend Running"
    }