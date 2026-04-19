from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.llm import generate_response
from app.memory import get_history, save_message
from app.tools import execute_tool

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    history = get_history(req.session_id)

    response = generate_response(req.message, history)

    # Check if tool call
    if response.get("tool"):
        tool_result = execute_tool(response["tool"], response["arguments"])
        reply = f"Executed {response['tool']}: {tool_result}"
    else:
        reply = response.get("content")

    save_message(req.session_id, "user", req.message)
    save_message(req.session_id, "assistant", reply)

    return ChatResponse(reply=reply)
