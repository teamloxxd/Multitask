from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text("👋 Welcome to the Multitask Bot!\nUse /help to see commands.")

@Client.on_message(filters.command("help"))
async def help(_, message: Message):
    await message.reply_text("""
🧰 Commands:
/leech <url> [-e]
/youtube <url>
/url <url>
/token <code>
/info
/telegraph (reply)
/thumb, /delthumb, /showthumb
/uptime, /restart

👑 Admin:
/ban <id>, /unban <id>
/broadcast <text>
/tokenusers, /status, /stats
""")