from pyrogram import Client, filters
from pyrogram.types import Message
import subprocess
import os

@Client.on_message(filters.command("leech"))
async def mega_leech(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /leech <mega link> [-e]")

    text = message.text.split()
    url = text[1]
    extract = "-e" in text

    filename = "file_from_mega"
    try:
        subprocess.run(["megadl", url, "--path", filename], check=True)
    except Exception as e:
        return await message.reply(f"❌ MEGA Download Failed: {e}")

    if not os.path.exists(filename):
        return await message.reply("❌ File not found after download.")

    if extract and filename.endswith(".zip"):
        import zipfile
        try:
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall("unzipped/")
            await message.reply_document("unzipped/")
        except Exception as e:
            return await message.reply(f"❌ Extraction Failed: {e}")
    else:
        await message.reply_document(filename)