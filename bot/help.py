from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
Setting up
1) Add this Bot to your Group and Make it Admin 
2) Add @Sstreamming_assist to your Group manually. 
Commands
=>> Vidio Playing 🎧
- /stream : Reply to Video or File That You Want To stream In Vc.
- /estream  : Stop the stream
- /start :Start the bot
- /help  :To Help You
- /ly   : To Get lyrics Of Song
- /vsearch : To Get Link From Youtube
- /quote: To Get Anime quote
- /sysinfo : To get sysinfo
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Chat", url="https://t.me/stylishuser"
                    )
                ]
            ]
        )
    )    
