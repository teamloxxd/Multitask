from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file, Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name="Multibot")

@Client.on_message(filters.command("telegraph"))
async def telegraph_upload(_, message: Message):
    if message.reply_to_message:
        r = message.reply_to_message
        if r.photo:
            path = await r.download()
            try:
                response = upload_file(path)
                await message.reply(f"📎 Uploaded to Telegraph:\nhttps://telegra.ph{response[0]['src']}")
            except Exception as e:
                await message.reply(f"❌ Upload failed: {e}")
        elif r.text or r.caption:
            content = r.text or r.caption
            page = telegraph.create_page(
                title="Shared via MultitaskBot",
                html_content=f"<p>{content}</p>"
            )
            await message.reply(f"📝 Telegraph link:\nhttps://telegra.ph/{page['path']}")
        else:
            await message.reply("⚠️ Reply to a photo or a text message.")
    else:
        await message.reply("❗ Use `/telegraph` by replying to a text or photo.")