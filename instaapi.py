import requests
import json

import secrets
import telegram

url = "https://instagram-scraper-20231.p.rapidapi.com/userinfo/instagram"

headers = {
	"X-RapidAPI-Key": secrets.instaapi_key,
	"X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
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
    limit = float(int(response.headers["X-RateLimit-Requests-Limit"]))
    remaining = float(int(response.headers["X-RateLimit-Requests-Remaining"]))
    percentage = (limit-remaining)*100/limit
    print(percentage)
    if percentage > 70:
        telegram.bot_sendtext(f"На Instagram Scraper 2023 {percentage}%")
    else:
        print("yay")