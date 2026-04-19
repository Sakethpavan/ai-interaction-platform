import requests
import json
import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2:latest")

SYSTEM_PROMPT = """
You are an AI assistant.

STRICT RULES:
- If a user asks to perform an action, you MUST return JSON.
- DO NOT respond with normal text if a tool can be used.
- ALWAYS return valid JSON for tool calls.

Available tools:
1. open_app(app_name)
2. search_google(query)

Examples:

User: open chrome
Response:
{
  "tool": "open_app",
  "arguments": { "app_name": "chrome" }
}

User: search cats
Response:
{
  "tool": "search_google",
  "arguments": { "query": "cats" }
}
"""

def generate_response(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for h in history:
        messages.append({"role": h["role"], "content": h["content"]})

    messages.append({"role": "user", "content": message})

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    })

    content = response.json()["message"]["content"]

    try:
        parsed = json.loads(content)
        return parsed
    except:
        return {"content": content}