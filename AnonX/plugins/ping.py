from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL, YAFA_CHANNEL, YAFA_NAME
from strings import get_command
from strings.filters import command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils import bot_sys_stats
from AnonX.utils.decorators.language import language
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


### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
)
@app.on_message(
    command(["بنك"])
)
@language
async def ping_com(client, message: Message, _):
    if not await check_is_joined(message):
        return
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Anon.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ),
        reply_markup=close_keyboard
    )
