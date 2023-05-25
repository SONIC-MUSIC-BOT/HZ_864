from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BANNED_USERS, YAFA_CHANNEL, YAFA_NAME
from strings import get_command
from strings.filters import command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils.database import is_music_playing, music_off
from AnonX.utils.decorators import AdminRightsCheck
from AnonX.utils.inline.play import close_keyboard


force_btn = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(   
              text=f"{YAFA_NAME}", url=f"{YAFA_CHANNEL}",)                        
        ],        
    ]
) 
async def check_is_joined(message):    
    try:
        userid = message.from_user.id
        status = await app.get_chat_member(f"{CHANNEL_SUDO}", userid)
        return True
    except Exception:
        await message.reply_text("**⌔︙  عليك الاشتراك في قناة البوت اولاً :**",reply_markup=force_btn,parse_mode="markdown",disable_web_page_preview=False)
        return False


# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_message(
    command(["اوكف","وقف"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Anon.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.first_name),
        reply_markup=close_keyboard
    )
