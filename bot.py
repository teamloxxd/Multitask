from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, PLUGIN_DIR
from scheduler import cleanup_tokens_job

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins={"root": PLUGIN_DIR})

if __name__ == "__main__":
    cleanup_tokens_job()
    print("Bot Started.")
    app.run()