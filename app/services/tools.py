import webbrowser
import os

def execute_tool(tool_name, args):
    if tool_name == "open_app":
        return open_app(args.get("app_name", ""))

    elif tool_name == "search_google":
        query = args.get("query", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searched for '{query}'"

    return "Unknown tool"


def open_app(app_name: str):
    app = app_name.lower()

    if app in ["chrome", "browser", "brave"]:
        if app == "brave":
            os.system("start brave")
            return "Brave opened"
        else:
            os.system("start chrome")
            return "Chrome opened"

    return f"Unknown app: {app}"
