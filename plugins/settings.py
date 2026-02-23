from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("settings"))
async def settings_cmd(client, message):
    btn = [[
        InlineKeyboardButton("Set Prefix", callback_data="set_prefix"),
        InlineKeyboardButton("Set Suffix", callback_data="set_suffix")
    ],[
        InlineKeyboardButton("Set Caption", callback_data="set_caption"),
        InlineKeyboardButton("Set Thumbnail", callback_data="set_thumb")
    ]]
    await message.reply_text("User Settings Panel", reply_markup=InlineKeyboardMarkup(btn))
