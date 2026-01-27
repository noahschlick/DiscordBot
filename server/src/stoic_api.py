import requests
import os
import json

BASE_URL = os.getenv("BASE_URL")
API_TOKEN = os.getenv("API_TOKEN")

async def getAnswer(user_query, conversation_history=None):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    params = {"input": user_query}
    if conversation_history:
        params["history"] = json.dumps(conversation_history)

    response = requests.get(f'{BASE_URL}/api', params=params, headers=headers)
    return response.json()