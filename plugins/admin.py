from pyrogram import Client, filters
from pyrogram.types import Message
from database import ban_user, unban_user, count_users, count_banned, count_token_users
import os
import time

start_time = time.time()

@Client.on_message(filters.command("ban") & filters.user(OWNER_ID))
async def ban(_, message: Message):
    if len(message.command) >= 2:
        user_id = int(message.command[1])
        ban_user(user_id)
        await message.reply("✅ User Banned.")
    else:
        await message.reply("❌ Provide user ID.")

@Client.on_message(filters.command("unban") & filters.user(OWNER_ID))
async def unban(_, message: Message):
    if len(message.command) >= 2:
        user_id = int(message.command[1])
        unban_user(user_id)
        await message.reply("✅ User Unbanned.")
    else:
        await message.reply("❌ Provide user ID.")

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(_, message: Message):
    if len(message.command) < 2:
        await message.reply("❌ Usage: /broadcast your_message")
        return
    text = message.text.split(None, 1)[1]
    from database import db
    users = db.users.find()
    success = 0
    for u in users:
        try:
            await _.send_message(u["_id"], text)
            success += 1
        except:
            pass
    await message.reply(f"✅ Sent to {success} users.")

@Client.on_message(filters.command("tokenusers") & filters.user(OWNER_ID))
async def token_users(_, message: Message):
    total = count_token_users()
    await message.reply(f"🪙 Token users: {total}")

@Client.on_message(filters.command("status") & filters.user(OWNER_ID))
async def status(_, message: Message):
    users = count_users()
    banned = count_banned()
    await message.reply(f"👤 Users: {users}\n🚫 Banned: {banned}")

@Client.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(_, message: Message):
    await status(_, message)

@Client.on_message(filters.command("uptime"))
async def uptime(_, message: Message):
    current = time.time()
    uptime = current - start_time
    hrs, rem = divmod(int(uptime), 3600)
    mins, secs = divmod(rem, 60)
    await message.reply(f"🕓 Uptime: {hrs}h {mins}m {secs}s")

@Client.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def restart_bot(_, message: Message):
    await message.reply("♻️ Restarting bot...")
    os.execv(sys.executable, ['python'] + sys.argv)