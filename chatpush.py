import requests

import telegram

url = 'https://api.chatpush.ru/api/v1/account'

data = {}

headers = {
    'Authorization': 'Bearer ',
}

response = requests.get(
    url,
    data=data,
    headers=headers,
    timeout=30
)

print(response.status_code)

result = response.json()
if response.status_code == 200:
    if int(float(result["account"]["total_amount"])) < 150000:
        telegram.bot_sendtext("На чатпуше менее 150к")
    else:
        print("yay")
