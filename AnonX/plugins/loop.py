from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BANNED_USERS, YAFA_CHANNEL, YAFA_NAME
from strings import get_command
from strings.filters import command
from AnonX import app
from AnonX.utils.database.memorydatabase import (get_loop,
                                                      set_loop)
from AnonX.utils.decorators import AdminRightsCheck


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
LOOP_COMMAND = get_command("LOOP_COMMAND")


@app.on_message(
    filters.command(LOOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_message(
    command(["كرر"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(cli, message: Message, _, chat_id):
    if not await check_is_joined(message):
        return
    usage = _["admin_24"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    if state.isnumeric():
        state = int(state)
        if 1 <= state <= 10:
            got = await get_loop(chat_id)
            if got != 0:
                state = got + state
            if int(state) > 10:
                state = 10
            await set_loop(chat_id, state)
            return await message.reply_text(
                _["admin_25"].format(
                    message.from_user.first_name, state
                )
            )
        else:
            return await message.reply_text(_["admin_26"])
    elif state.lower() == "enable":
        await set_loop(chat_id, 10)
        return await message.reply_text(
            _["admin_25"].format(message.from_user.first_name, state)
        )
    elif state.lower() == "disable":
        await set_loop(chat_id, 0)
        return await message.reply_text(_["admin_27"])
    else:
        return await message.reply_text(usage)
