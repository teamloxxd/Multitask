from pyrogram import Client, filters
from pyrogram.types import Message
import subprocess
import os
import shutil

@Client.on_message(filters.command("mega"))
async def mega_leech(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /mega <mega link> [-e]")

    text = message.text.split()
    url = text[1]
    extract = "-e" in text

    try:
        # Get filename from URL (safer naming)
        output = subprocess.check_output(["megadl", "--print-names", url]).decode().strip()
        if not output:
            return await message.reply("❌ Could not get file name from MEGA URL.")
        filename = output.split("\n")[0]

        # Download the file
        await message.reply("⏬ Downloading file from MEGA...")
        subprocess.run(["megadl", url, "--path", filename], check=True)

        if not os.path.exists(filename):
            return await message.reply("❌ File not found after download.")

        # If -e and zip, extract
        if extract and filename.endswith(".zip"):
            extracted_folder = "unzipped"
            shutil.unpack_archive(filename, extracted_folder)
            for root, _, files in os.walk(extracted_folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    await message.reply_document(full_path)
                    os.remove(full_path)
            shutil.rmtree(extracted_folder)
        else:
            await message.reply_document(filename)
            os.remove(filename)

    except subprocess.CalledProcessError:
        return await message.reply("❌ MEGA Download Failed. Make sure the link is correct.")
    except Exception as e:
        return await message.reply(f"❌ Error: `{str(e)}`")
