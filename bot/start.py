from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply_text(f"**I am A advanced Anime Theme VC Video Player created for playing Video in the voice chats of Telegram Groups & Channels. \n\n**Type /help To View Comands:-** __ \n1) Type /info To View Devs`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Dev", url="https://t.me/Monstar_0")
                                    ]]
                            ))
   else:
      await m.reply_text(f"**Hola, Join @StylishUser")
