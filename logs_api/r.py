import requests
import json

response = requests.get("https://logs.tf/api/v1/log?limit=5000")

jdata = response.json()

for i, log in enumerate(jdata["logs"]):
    with open(f"logs/{log['id']}.json", "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=4)
