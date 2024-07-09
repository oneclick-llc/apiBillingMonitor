import requests
import json

import secrets
import telegram

url = "https://v1.rocketapi.io/usage"

headers = {
	"Content-Type": "application/json",
	"Authorization": "Token " + secrets.insta_rocket_api_key
}

response = requests.get(url, headers=headers)

print(response.json())
print(response.headers)
'''
import json
with open('data.json', 'w') as f:
    json.dump(response.json(), f)
'''
if response.status_code == 200:
    limit = int(response.json()["limit"])
    requests = int(response.json()["requests"])
    percentage = (requests)*100/limit
    print(percentage)
    if percentage > 60:
        telegram.bot_sendtext(f"Instagram RocketAPI истрачен на {percentage:.2f}%\nПотрачено: {requests:,} запросов\nОсталось: {limit - requests:,} запросов\nЛимит: {limit:,}")
    else:
        print("yay")