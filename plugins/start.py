from asyncio import sleep
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import START_PIC, FLOOD, ADMIN 
from lazydeveloper.utils import initate_lazy_verification



@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user           
    txt=f"👋 Hello {user.mention} \n\nI am an Advance server uploader BOT with custom filename support.\n\n<blockquote>Send me any video or document !</blockquote>"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton('⚡️ About', callback_data='about'),
        InlineKeyboardButton('🤕 Help', callback_data='help')
        ],
        [
        InlineKeyboardButton("🐱‍👤 About Developer 🐱‍👤", callback_data='dev')
        ]
        ])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button, )       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True, )
    
@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")
