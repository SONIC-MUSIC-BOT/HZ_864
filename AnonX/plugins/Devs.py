import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram



@app.on_message(
    command(["سورس سونك","سورس","السورس","سونك سورس", "source"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b5281f70c4dc630ee3e62.jpg",
        caption=f"""
╭──── • ◈ • ────╮ 

⌔︙معلومات السورس

⌔︙[سورس سونك](https://t.me/SONIC_source)

⌔︙[حسين مطور السورس](https://t.me/Huseenytiq)

⌔︙[مساعدة مطور السورس](https://t.me/MZ_864)

⌔︙[بوت تواصل السورس](https://t.me/Huseenytiq_bot)

⌔︙[مجموعة الدعم](https://t.me/SONIC_source_SUPPORT)

⌔︙[✲°• منتدى منارة القانتين •°✲](https://t.me/Manarat_Alqaniten)

╰──── • ◈ • ────╯ 
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطور السورس", url=f"https://t.me/Huseenytiq"), 
                ],[
                    InlineKeyboardButton(
                        "مساعدة مطور السورس", url=f"https://t.me/MZ_864"),
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗡𝗜𝗖 𝗦𝗢𝗨𝗥𝗖𝗘 ⚡", url=f"https://t.me/SONIC_source"),
                ],[
                    InlineKeyboardButton(
                        "✲°• منتدى منارة القانتين •°✲", url=f"t.me/Manarat_Alqaniten"),
                ],

            ]

        ),

    )
@app.on_message(
   command(["المطور","مطور","المبرمج","مطور السورس","حسين صلاح"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(5301059909)
  user = await client.get_chat(5301059909)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(5301059909,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""⌔︙معلومات المطور\n\nn⌔︙ المطور | - {usr.mention}
                       
⌔︙ معرف المطور | - @{usr.username}
                       
⌔︙ بايو المطور | - {Bio}     
                         
⌔︙ ايدي المطور | - 5301059909  """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(5301059909, f"⌔︙عزيزي المطور {zoharyus}\n\n⌔︙  {message.from_user.mention} بحاجه اليك \n\n⌔︙ ايديه : {sender_id} \n\n⌔︙ اسمه : {sender_name} \n\n⌔︙ رابط الرساله : {message_link} \n\n⌔︙ رابط المجموعه : {invitelink}")
@app.on_message(
    command(["المطور2","مساعدة مطور السورس","أولسنا على الحق","المطوره","مطور2","العلويه","العلوية"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(208837121)
  user = await client.get_chat(208837121)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(208837121,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""⌔︙معلومات المطور\n\n⌔︙ المطور | - {usr.mention}
                       
⌔︙ معرف المطور | - @{usr.username}
                       
⌔︙ بايو المطور | - {Bio}      
                         
⌔︙ ايدي المطور | - 208837121 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(208837121, f"⌔︙عزيزي المطور {zoharyus}\n\n⌔︙ {message.from_user.mention} بحاجه اليك \n\n⌔︙ ايديه : {sender_id} \n\n⌔︙ اسمه : {sender_name} \n\n⌔︙ رابط الرساله : {message_link} \n\n⌔︙ رابط المجموعه : {invitelink}")
                        
