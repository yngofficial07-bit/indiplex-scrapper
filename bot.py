import os
from pyrogram import Client
from flask import Flask
from threading import Thread

# 1. Flask server banayenge jo Render ko lagega ki website chal rahi hai
flask_app = Flask(__name__)
@flask_app.route('/')
def home():
    return "Indiplex Engine is Running!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=8080)

# 2. Tera Bot Logic
API_ID = 38525545
API_HASH = "25d7cd7f859b83bfe1761fd93079fe63"
BOT_TOKEN = "APNA_TOKEN_YAHAN_DALO"

app = Client("indiplex_worker", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    # Flask ko alag thread mein chalao
    Thread(target=run_flask).start()
    # Bot ko start karo
    print("Indiplex Bot is LIVE...")
    app.run()
