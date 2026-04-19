def fallback_tool_detection(message: str):
    msg = message.lower()

    if "open" in msg:
        if "chrome" in msg or "browser" in msg:
            return {
                "tool": "open_app",
                "arguments": {"app_name": "chrome"}
            }

        if "brave" in msg:
            return {
                "tool": "open_app",
                "arguments": {"app_name": "brave"}
            }

    if "search" in msg:
        query = msg.replace("search", "").strip()
        return {
            "tool": "search_google",
            "arguments": {"query": query}
        }

    return None
