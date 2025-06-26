from pyrogram import Client, filters
from pyrogram.types import Message
import os

THUMB_DIR = "downloads/thumbs"

@Client.on_message(filters.command("thumb"))
async def save_thumb(_, message: Message):
    if message.reply_to_message and message.reply_to_message.photo:
        path = f"{THUMB_DIR}/{message.from_user.id}.jpg"
        await message.reply_to_message.download(file_name=path)
        await message.reply("✅ Thumbnail saved!")
    else:
        await message.reply("⚠️ Reply to a photo with /thumb to save it.")

@Client.on_message(filters.command("delthumb"))
async def del_thumb(_, message: Message):
    path = f"{THUMB_DIR}/{message.from_user.id}.jpg"
    if os.path.exists(path):
        os.remove(path)
        await message.reply("🗑️ Thumbnail deleted.")
    else:
        await message.reply("❌ No thumbnail found.")

@Client.on_message(filters.command("showthumb"))
async def show_thumb(_, message: Message):
    path = f"{THUMB_DIR}/{message.from_user.id}.jpg"
    if os.path.exists(path):
        await message.reply_photo(photo=path, caption="🖼️ Your current thumbnail:")
    else:
        await message.reply("⚠️ No thumbnail set.")