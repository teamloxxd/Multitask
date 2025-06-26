from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import yt_dlp

@Client.on_message(filters.command("youtube"))
async def youtube_handler(bot, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /youtube <URL>")

    url = message.text.split(maxsplit=1)[1]

    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get("title", "Unknown Title")
            formats = info.get("formats", [])
    except Exception as e:
        return await message.reply(f"❌ Error: {str(e)}")

    buttons = []
    for f in formats:
        if f.get("vcodec") != "none" and f.get("acodec") != "none":
            f_url = f.get("url")
            label = f"{f.get('format')} - {f.get('format_note') or ''}"
            buttons.append([InlineKeyboardButton(label[:50], url=f_url)])

        if len(buttons) >= 10:
            break

    if not buttons:
        return await message.reply("⚠️ No downloadable formats found.")

    await message.reply(
    f"""🎬 **{title}**
📥 Select quality from below:""",
    reply_markup=InlineKeyboardMarkup(buttons)
)
