from fastapi import APIRouter
from ..database.schemas import ChatRequest
from ..services.ai_service import ask_ai

router = APIRouter()

@router.post("/chat")

def chat(chat:ChatRequest):

    response = ask_ai(chat.message)

    return {"response":response}