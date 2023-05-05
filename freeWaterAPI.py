import requests

async def getAnswer(user_querie):
    response = requests.get(f'https://freewaterchatbotapi.onrender.com/api?input={user_querie}')
    return response.json()