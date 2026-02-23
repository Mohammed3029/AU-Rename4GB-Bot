from pyrogram import Client, filters

@Client.on_message(filters.command("about"))
async def about_cmd(client, message):
    await message.reply_text(
        "AU Rename 4GB Bot\n"
        "Developer: Mohammed\n"
        "Python + Pyrogram\n"
        "MongoDB + Render Deploy"
    )
