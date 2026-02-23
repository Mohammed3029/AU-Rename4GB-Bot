from pyrogram import Client, filters

@Client.on_message(filters.command("metadata"))
async def meta_cmd(client, message):
    await message.reply("Metadata system active (title, author, encoder)")
