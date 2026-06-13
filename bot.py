import requests
import json

USERNAME = "alnoooo"

url = f"https://api.github.com/users/{USERNAME}/repos"

repos = requests.get(url).json()

projects = []

for repo in repos:

    projects.append(
        {
            "title": repo["name"],
            "description": repo["description"],
            "github": repo["html_url"]
        }
    )

with open(
    "projects.json",
    "w"
) as file:

    json.dump(
        projects,
        file,
        indent=4
    )

print("projects.json generated successfully!")