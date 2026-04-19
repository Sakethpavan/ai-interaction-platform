import webbrowser
import os
import shutil

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

    if app in ["chrome", "browser"]:
        # check if chrome exists
        if shutil.which("chrome"):
            os.system("start chrome")
            return "Chrome opened"

        # fallback to brave
        if shutil.which("brave"):
            os.system("start brave")
            return "Brave opened"

        return "No supported browser found"

    if app == "brave":
        if shutil.which("brave"):
            os.system("start brave")
            return "Brave opened"
        return "Brave not installed"

    return f"Unknown app: {app}"