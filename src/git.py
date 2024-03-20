import json
import os

import requests

from utils import setup_custom_logger

LOGGER = setup_custom_logger("root")

def create_comment(org, repo, pr_number, comment):
    token = os.environ["GITHUB_TOKEN"]
    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    body = json.dumps({"body": comment})

    url = f"https://api.github.com/repos/{org}/{repo}/issues/{pr_number}/comments"
    res = requests.post(url, body, headers=headers)
    LOGGER.info(res.json())
    return res.json()
