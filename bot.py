from pyrogram import Client
from config import Config
from database import db

app = Client(
    "au_rename4gb",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    db.connect()
    print("AU Rename 4GB Bot Started...")
    app.run()
