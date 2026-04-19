from pydantic import BaseModel

class ChatRequest(BaseModel):
    userId: str
    message: str
    session_id: str

class ChatResponse(BaseModel):
    reply: str
