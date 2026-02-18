import os
import asyncio
import threading
from flask import Flask
from pyrogram import Client, filters

# --- Flask Server for Render Port Fix ---
flask_app = Flask(__name__)

@flask_app.route('/')
def health_check():
    return "Indiplex Bot is Running!"

def run_flask():
    # Render hamesha port 10000 mangta hai
    flask_app.run(host="0.0.0.0", port=10000)

# --- Python 3.14+ Event Loop Fix ---
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# --- Bot Configuration ---
API_ID = 38525545 
API_HASH = "25d7cd7f859b83bfe1761fd93079fe63"
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGO_URL = os.environ.get("MONGO_URL")

app = Client("indiplex_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Bhai, Indiplex Bot ekdum LIVE hai! 🔥")

if __name__ == "__main__":
    # Flask ko alag thread mein chalao
    threading.Thread(target=run_flask, daemon=True).start()
    print("Indiplex Bot is LIVE...")
    app.run()
