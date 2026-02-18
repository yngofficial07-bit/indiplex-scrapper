import os
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient

# --- CONFIG ---
API_ID = 38525545
API_HASH = "25d7cd7f859b83bfe1761fd93079fe63"
BOT_TOKEN = "APNA_BOT_TOKEN_YAHAN_DALO" # BotFather se mila hua token
MONGO_URL = "mongodb+srv://yngofficial07_db_user:9IKoDnZiTZVpe19V@cluster0.tmefhsm.mongodb.net/?appName=Cluster0"

# --- INITIALIZE ---
app = Client("indiplex_worker", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client["indiplex_db"]

@app.on_message(filters.command("find") & filters.private)
async def search_movie(client, message):
    if len(message.command) < 2:
        await message.reply("Bhai, movie ka naam toh likh! (Example: /find Jawan)")
        return

    query = message.text.split(None, 1)[1]
    await message.reply(f"🔍 Searching for **{query}** in Telegram...")

    # Yahan hum movies search karenge (Abhi basic logic hai)
    # File milte hi hum use DB mein save karenge
    await db.movies.insert_one({
        "title": query,
        "status": "searching",
        "requested_by": message.from_user.id
    })
    
    await message.reply(f"✅ Your request for **{query}** is added to Indiplex database!")

print("Indiplex Bot is LIVE 24/7...")
app.run()
