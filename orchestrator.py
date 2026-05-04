import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

# 1. Setup
load_dotenv()

# --- THE TOOLS ---
def github_tool(username, repo):
    print(f"🔍 [TOOL] Fetching GitHub data...")
    url = f"https://api.github.com/repos/{username}/{repo}"
    try:
        r = requests.get(url)
        data = r.json()
        return {"stars": data.get("stargazers_count", 0), "forks": data.get("forks_count", 0)}
    except:
        return {"stars": 0, "forks": 0}

def slack_tool(stats):
    print("\n--- 📡 [TOOL] SLACK NOTIFICATION ---")
    print(f"Post: Repo has {stats['stars']} Stars.")
    print("------------------------------------\n")

def file_tool(data):
    """Saves the result to a local text file."""
    filename = "workflow_log.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] Report: {json.dumps(data)}\n")
    print(f"💾 [TOOL] Report saved to {filename}")

# --- THE BRAIN ---
def orchestrate(user_request):
    print(f"🤖 User Request: {user_request}")
    plan = []
    
    # Intent Detection
    if "github" in user_request.lower(): plan.append("GITHUB")
    if "slack" in user_request.lower(): plan.append("SLACK")
    if "save" in user_request.lower() or "record" in user_request.lower(): plan.append("SAVE")

    # Execution
    context = {}
    for task in plan:
        if task == "GITHUB":
            context['data'] = github_tool("tanusha-19", "AI-Workflow-Builder")
        if task == "SLACK" and 'data' in context:
            slack_tool(context['data'])
        if task == "SAVE" and 'data' in context:
            file_tool(context['data'])

if __name__ == "__main__":
    # Test a full complex request
    orchestrate("Check github and save the record")