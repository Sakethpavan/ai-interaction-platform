import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

SYSTEM_PROMPT = """
You are an AI assistant.

Available tools:
1. open_app(app_name)
2. search_google(query)

If a tool is needed, respond ONLY in JSON:
{
  "tool": "tool_name",
  "arguments": { ... }
}

Otherwise respond normally.
"""

def generate_response(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for h in history:
        messages.append({"role": h["role"], "content": h["content"]})

    messages.append({"role": "user", "content": message})

    response = requests.post(OLLAMA_URL, json={
        "model": "llama3",
        "messages": messages,
        "stream": False
    })

    content = response.json()["message"]["content"]

    try:
        import json
        parsed = json.loads(content)
        return parsed
    except:
        return {"content": content}
