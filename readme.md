# apiBillingMonitor

Набор скриптов на python, которые собирают важные для бизнес задач метрики и отправляют алетры в Telegram по достижению заданных в .env threshold

Пример содержимого .env
```
#secrets
INSTA_API=""
BOT_TOKEN=""
CHAT_ID=""
CHATPUSH_BEARER=""

#config
CHATPUSH_TRESHOLD=300000
CHATPUSH_DELTA_TRESHOLD=1500
PUSHGATEWAY_IP="localhost:9091"
```