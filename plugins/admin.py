from pyrogram import Client, filters
from config import Config

@Client.on_message(filters.user(Config.OWNER_ID) & filters.command("stats"))
async def stats_cmd(client, message):
    await message.reply("Admin panel active")
