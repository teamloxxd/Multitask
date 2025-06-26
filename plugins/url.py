from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import os

@Client.on_message(filters.command("url"))
async def url_to_file(bot, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: `/url <direct_download_link>`", quote=True)

    url = message.text.split(maxsplit=1)[1]
    file_name = url.split("/")[-1] or "downloaded_file"

    try:
        response = requests.get(url, stream=True, timeout=15)
        if response.status_code != 200:
            return await message.reply("❌ Failed to download the file.")

        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(1024 * 1024):
                if chunk:
                    f.write(chunk)

        await bot.send_document(
            chat_id=message.chat.id,
            document=file_name,
            caption="✅ File downloaded from URL"
        )
        os.remove(file_name)

    except Exception as e:
        await message.reply(f"❌ Error: `{str(e)}`")
