from pyrogram import Client, filters
from database import db
import os

@Client.on_message(filters.document | filters.video | filters.audio)
async def rename_handler(client, message):
    user = db.get_user(message.from_user.id)
    prefix = user.get("prefix", "")
    suffix = user.get("suffix", "")
    caption = user.get("caption", "")

    file = message.document or message.video or message.audio
    old = file.file_name
    name = f"{prefix}{old}{suffix}"

    msg = await message.reply("Downloading...")
    path = await client.download_media(message)
    new_path = os.path.join(os.path.dirname(path), name)
    os.rename(path, new_path)

    await msg.edit("Uploading...")
    await message.reply_document(new_path, caption=caption)
    os.remove(new_path)
