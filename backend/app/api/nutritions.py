from fastapi import APIRouter
from ..services.ai_service import ask_ai

router = APIRouter()

@router.get("/plan")

def nutrition(weight:float, goal:str):

    prompt = f"""
Create a healthy diet plan.

Weight: {weight}
Goal: {goal}
"""

    result = ask_ai(prompt)

    return {"nutrition_plan":result}