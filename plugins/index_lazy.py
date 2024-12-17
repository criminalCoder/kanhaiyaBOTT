
# from lazydeveloper.lazydb import db
# from config import * 
# from pyrogram import Client, filters
# import logging
# import asyncio
# from pyrogram import Client, filters, enums
# from pyrogram.errors import FloodWait
# from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified

# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# import re
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# lock = asyncio.Lock()


# # async def index_movie_database(bot):
# #     async for message in bot.get_chat_history(MOVIE_DATABASE):
# #         if message.text:
# #             try:
# #                 title, link = message.text.split("\n")[0], message.text.split("\n")[1]
# #                 # Add to MongoDB
# #                 await db.add_movie(title, link)
# #             except IndexError:
# #                 continue
# #     print("Database indexing complete.")


# async def index_movie_database(bot, forwarded_message):
#     """
#     Index movies in the database channel starting from the ID of the forwarded message and going backwards.
#     """
#     try:
#         # Get the message ID of the forwarded message
#         start_message_id = forwarded_message.forward_from_message_id
        
#         # Iterate over the message history starting from the specific message
#         async for message in bot.get_chat_history(MOVIE_DATABASE, offset_id=start_message_id):
#             if message.text:
#                 try:
#                     # Extract title and link from the message text
#                     lines = message.text.split("\n")
#                     if len(lines) >= 2:
#                         title, link = lines[0], lines[1]
                        
#                         # Add to MongoDB
#                         await db.add_movie(title, link)
#                 except Exception as e:
#                     print(f"Skipping message due to error: {e}")
#                     continue

#         print("Database indexing complete.")
    
#     except Exception as e:
#         print(f"Error while indexing: {e}")

# @Client.on_message(filters.command("index") & filters.reply)
# async def start_indexing(bot, message):
#     """
#     Trigger the indexing process using a forwarded message.
#     """
#     if not message.reply_to_message or not message.reply_to_message.forward_from_message_id:
#         await message.reply_text("Please reply to a forwarded message from the database channel.")
#         return
    
#     await message.reply_text("Indexing database, please wait...")
#     await index_movie_database(bot, message.reply_to_message)
#     await message.reply_text("Indexing complete!")

# # @Client.on_message((filters.forwarded | (filters.regex("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")) & filters.text ) & filters.private & filters.incoming)
# # async def send_for_index(bot, message):
# #     if message.text:
# #         regex = re.compile("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
# #         match = regex.match(message.text)
# #         if not match:
# #             return await message.reply('Invalid link')
# #         chat_id = match.group(4)
# #         last_msg_id = int(match.group(5))
# #         if chat_id.isnumeric():
# #             chat_id  = int(("-100" + chat_id))
# #     elif message.forward_from_chat.type == enums.ChatType.CHANNEL:
# #         last_msg_id = message.forward_from_message_id
# #         chat_id = message.forward_from_chat.username or message.forward_from_chat.id
# #     else:
# #         return
# #     try:
# #         await bot.get_chat(chat_id)
# #     except ChannelInvalid:
# #         return await message.reply('This may be a private channel / group. Make me an admin over there to index the files.')
# #     except (UsernameInvalid, UsernameNotModified):
# #         return await message.reply('Invalid Link specified.')
# #     except Exception as e:
# #         logger.exception(e)
# #         return await message.reply(f'Errors - {e}')
# #     try:
# #         k = await bot.get_messages(chat_id, last_msg_id)
# #     except:
# #         return await message.reply('Make Sure That I am An Admin In The Channel, if channel is private')
# #     if k.empty:
# #         return await message.reply('This may be group and i am not a admin of the group.')

# #     if message.from_user.id in ADMIN:
# #         buttons = [
# #             [
# #                 InlineKeyboardButton('Yes',
# #                                      callback_data=f'index#accept#{chat_id}#{last_msg_id}#{message.from_user.id}')
# #             ],
# #             [
# #                 InlineKeyboardButton('close', callback_data='close_data'),
# #             ]
# #         ]
# #         reply_markup = InlineKeyboardMarkup(buttons)
# #         return await message.reply(
# #             f'Do you Want To Index This Channel/ Group ?\n\nChat ID/ Username: <code>{chat_id}</code>\nLast Message ID: <code>{last_msg_id}</code>',
# #             reply_markup=reply_markup)


# #     await message.reply('❤')
