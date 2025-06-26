cat > README.md << 'EOF'
# 📦 Multitask Telegram Bot

A powerful Telegram bot with multitasking features like file leeching, YouTube download, URL to file, token-based access system, custom thumbnails, and admin tools — powered by Pyrogram.

---

## ✨ Features

| Feature | Command |
|--------|---------|
| 📥 Leech (w/ extract) | `/leech <link> [-e]` |
| 🎞 YouTube Quality Select | `/youtube <url>` |
| 🌐 URL to File | `/url <url>` |
| 🧾 User Info | `/info` |
| 🖼 Thumbnail | `/thumb`, `/showthumb`, `/delthumb` |
| 📎 Telegraph | `/telegraph` (reply to text/photo) |
| 🔗 Token System | `/token <code>` (via InshortURL) |
| 👥 Admin Tools | `/ban`, `/unban`, `/broadcast`, `/status`, `/tokenusers`, `/stats` |
| 🔄 Restart Bot | `/restart`, `/uptime` |
| 🧠 MongoDB Integration | User/token/ban tracking |
| 📤 Dump Channel Support | Save all uploads |
| 🧹 Token Expiry | Auto background cleanup |

---

## 🛠 Setup Guide

### 1. Install Requirements

\`\`\`bash
pip3 install -r requirements.txt
\`\`\`

### 2. Fill `config.py`

\`\`\`python
API_ID = "Your Telegram API ID"
API_HASH = "Your API Hash"
BOT_TOKEN = "Your Bot Token"

MONGO_URI = "Your MongoDB URI"
DUMP_CHANNEL = -1001234567890
LOG_CHANNEL = -1001234567890

SHORTLINK_API = "Your InshortURL API Key"
SHORTLINK_SITE = "https://inshorturl.com/api"
TOKEN_EXPIRE_TIME = 7200  # In seconds

PLUGIN_DIR = "plugins"
\`\`\`

### 3. Run the Bot

\`\`\`bash
python3 bot.py
\`\`\`

Or run in `screen`:

\`\`\`bash
screen -S multitask
python3 bot.py
\`\`\`

---

## 📁 Folder Structure

\`\`\`
.
├── bot.py
├── config.py
├── database.py
├── scheduler.py
├── requirements.txt
├── plugins/
│   ├── start.py
│   ├── admin.py
│   ├── mega.py
│   ├── youtube.py
│   ├── telegraph.py
│   └── thumb.py
└── downloads/thumbs/
\`\`\`

---

## 👨‍💻 Developer

Made with ❤️ by [@teamloxxd](https://github.com/teamloxxd)

---

## 📜 License

MIT License
EOF
