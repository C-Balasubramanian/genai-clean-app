from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_service import ask_ai

router = APIRouter(prefix="/chat")

class ChatRequest(BaseModel):
    message: str

@router.post("/")
def chat_api(req: ChatRequest):
    print("Incoming message:", req.message)

    try:
        reply = ask_ai(req.message)
        print("AI reply:", reply)
        return {"reply": reply}
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))

