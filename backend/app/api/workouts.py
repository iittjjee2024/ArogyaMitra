from fastapi import APIRouter
from ..services.ai_service import ask_ai

router = APIRouter()

@router.get("/plan")

def workout(age:int, weight:float, goal:str):

    prompt = f"""
Create a weekly workout plan.

Age: {age}
Weight: {weight}
Goal: {goal}

Include exercises and sets.
"""

    result = ask_ai(prompt)

    return {"workout_plan":result}