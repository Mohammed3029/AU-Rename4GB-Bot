from pyrogram import Client, filters
from config import Config

@Client.on_message(filters.private)
async def force_sub(client, message):
    if not Config.FORCE_SUB:
        return
