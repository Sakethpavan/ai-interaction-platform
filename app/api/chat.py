from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.core.llm import generate_response
from app.services.memory import get_history, save_message
from app.services.tools import execute_tool
from app.services.fallback import fallback_tool_detection

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    history = get_history(req.session_id)

    response = generate_response(req.message, history)

    print("LLM RESPONSE:", response)

    # fallback if LLM fails to call tool
    if not response.get("tool"):
        fallback = fallback_tool_detection(req.message)
        if fallback:
            response = fallback

    # execute tool if present
    if response.get("tool"):
        tool_result = execute_tool(response["tool"], response["arguments"])
        reply = f"{tool_result}"
    else:
        reply = response.get("content")

    save_message(req.session_id, "user", req.message)
    save_message(req.session_id, "assistant", reply)

    return ChatResponse(reply=reply)