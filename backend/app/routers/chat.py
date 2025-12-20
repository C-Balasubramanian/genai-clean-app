from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_service import ask_ai

router = APIRouter(prefix="/chat")

class ChatRequest(BaseModel):
    message: str

@router.post("/")
def chat_api(req: ChatRequest):
    try:
        reply = ask_ai(req.message)
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
