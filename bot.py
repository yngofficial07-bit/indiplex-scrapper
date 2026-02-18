import os
import asyncio
import threading
from flask import Flask
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient

# --- Flask Server for Render Port Fix ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health_check(): return "Indiplex Engine is Running!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=10000)

# --- Python 3.14+ Event Loop Fix ---
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# --- Config ---
API_ID = 38525545 
API_HASH = "25d7cd7f859b83bfe1761fd93079fe63"
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGO_URL = os.environ.get("MONGO_URL")

# --- Database Setup ---
mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client.get_database("indiplex_db")
movies_col = db.get_collection("movies")

# --- Bot Client ---
app = Client("indiplex_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Ek Number Bhai! Movie ka naam likho, main dhoond kar deta hoon. 🔥")

# --- Search Logic ---
@app.on_message(filters.text & ~filters.command(["start", "help"]))
async def search_movie(client, message):
    query = message.text
    # MongoDB mein movie dhoondna
    movie = await movies_col.find_one({"name": {"$regex": query, "$options": "i"}})
    
    if movie:
        await message.reply_text(f"🎬 **Movie Mil Gayi!**\n\n✅ Name: {movie['name']}\n🔗 Link: {movie['link']}")
    else:
        await message.reply_text("❌ Sorry Bhai, ye movie abhi database mein nahi hai.")

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    print("Indiplex Engine Started...")
    app.run()
