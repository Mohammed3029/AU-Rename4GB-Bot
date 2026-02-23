from pyrogram import Client, filters

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text(
        "Commands:\n"
        "/start - Start bot\n"
        "/settings - User settings\n"
        "Send any file/video/audio up to 4GB to rename"
    )
