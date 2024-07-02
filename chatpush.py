import requests
import secrets
import telegram

url = 'https://api.chatpush.ru/api/v1/account'

data = {}

headers = {
    'Authorization': 'Bearer ' + secrets.chatpush_bearer,
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
    money = int(float(result["account"]["total_amount"]))
    if money < secrets.chatpush_delta_threshold:
        telegram.bot_sendtext(f"На чатпуше {money:,} рэ")
    else:
        print(money, "yay")
