from fastapi import APIRouter

from app.services.ai_agent import coach

router = APIRouter(
    prefix="/ai",
    tags=["AI Coach"]
)

@router.get("/workout")

def ai_workout(weight: float, goal: str):

    return coach.generate_workout(
        weight,
        goal
    )

@router.get("/diet")

def ai_diet(weight: float):

    return {
        "diet": coach.generate_diet(weight)
    }
