import requests
import json
import os
import base64

USERNAME = "alnoooo"

url = f"https://api.github.com/users/{USERNAME}/repos"
repos = requests.get(url).json()

projects = []

repos.sort(
    key=lambda x: x["updated_at"],
    reverse=True
)


for repo in repos:

    if repo["name"] == "portfolio":
        continue

    projects.append(
        {
            "title": repo["name"],
            "description": repo["description"] or "GitHub Automation Project",
            "github": repo["html_url"]
        }
    )

json_content = json.dumps(
    projects,
    indent=4
)

TOKEN = os.getenv("PAT_TOKEN")

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

repo_api = (
    "https://api.github.com/repos/"
    "alnoooo/portfolio/contents/projects.json"
)

current = requests.get(
    repo_api,
    headers=headers
).json()

payload = {
    "message": "Auto update projects.json",
    "content": base64.b64encode(
        json_content.encode()
    ).decode(),
    "sha": current["sha"]
}

response = requests.put(
    repo_api,
    headers=headers,
    json=payload
)

print(response.status_code)
print("Portfolio projects.json updated!")