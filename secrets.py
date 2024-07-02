import dotenv

#SECRETS
env_path = ".env"
instaapi_key = dotenv.get_key(env_path, "INSTA_API")
bot_token = dotenv.get_key(env_path, "BOT_TOKEN")
bot_chatID = dotenv.get_key(env_path, "CHAT_ID")
chatpush_bearer = dotenv.get_key(env_path, "CHATPUSH_BEARER")

#CONFIG
chatpush_threshold = int(dotenv.get_key(env_path, "CHATPUSH_TRESHOLD"))
chatpush_delta_threshold = int(dotenv.get_key(env_path, "CHATPUSH_DELTA_TRESHOLD"))


