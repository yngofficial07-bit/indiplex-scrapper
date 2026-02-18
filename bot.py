import os
import asyncio
from pyrogram import Client, filters

# Python 3.14+ compatibility fix
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Render ke Environment Variables se data uthana
API_ID = 38525545  # [cite: 2026-02-14]
API_HASH = "25d7cd7f859b83bfe1761fd93079fe63"  # [cite: 2026-02-14]
BOT_TOKEN = os.environ.get("BOT_TOKEN")  #
MONGO_URL = os.environ.get("MONGO_URL")  #

# Bot Client Setup
app = Client(
    "indiplex_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Ek Number Bhai! Indiplex Bot Live Hai. 🔥")

print("Indiplex Bot is LIVE...")
app.run()
