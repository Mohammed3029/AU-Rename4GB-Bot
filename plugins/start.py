from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    btn = [[
        InlineKeyboardButton("Settings", callback_data="settings"),
        InlineKeyboardButton("Help", callback_data="help")
    ]]
    await message.reply_text(
        "**AU Rename 4GB Bot**\n\nAuto Rename | Metadata | Thumbnails | Sequence | 4GB Support",
        reply_markup=InlineKeyboardMarkup(btn)
    )
