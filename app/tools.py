import webbrowser
import os

def execute_tool(tool_name, args):
    if tool_name == "open_app":
        app = args.get("app_name", "").lower()

        if app == "chrome":
            os.system("start chrome")  # Windows
            return "Chrome opened"

        return f"Unknown app: {app}"

    elif tool_name == "search_google":
        query = args.get("query", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searched for {query}"

    return "Unknown tool"
