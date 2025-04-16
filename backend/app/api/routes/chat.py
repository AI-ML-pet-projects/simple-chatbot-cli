from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.chat_service import chat_service

router = APIRouter()

class MessageRequest(BaseModel):
    message: str
    chat_id: str = None

class MessageResponse(BaseModel):
    message: str
    chat_id: str

@router.post("/chat", response_model=MessageResponse)
async def send_message(request: MessageRequest):
    try:
        if not request.chat_id:
            # Create new chat if no chat_id provided
            request.chat_id = chat_service.create_chat()
        
        response = chat_service.send_message(request.chat_id, request.message)
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat/new", response_model=MessageResponse)
async def create_new_chat():
    chat_id = chat_service.create_chat()
    return {"message": "New chat created", "chat_id": chat_id} 