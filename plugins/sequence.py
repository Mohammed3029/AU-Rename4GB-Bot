from pyrogram import Client, filters
from database import db

@Client.on_message(filters.command("sequence"))
async def seq_cmd(client, message):
    db.set_user(message.from_user.id, {"sequence": 1})
    await message.reply("Sequence mode enabled")
