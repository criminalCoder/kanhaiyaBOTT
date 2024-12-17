# from lazydeveloper.lazydb import db
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from pyrogram import enums, Client, filters
# import re
# import asyncio
# import re
# import ast
# import math
# import random
# import pytz
# from config import *
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# async def search_movie(query, offset=0, limit=10):
#     return await db.search_movies(query, offset=offset, limit=limit)

# @Client.on_message(filters.group | filters.private & filters.text & filters.incoming)
# async def filterlazy(client, message):
#     await auto_filter(client, message)

# def normalize_query(query):
#     stop_words = ["in", "upload", "series", "full", "horror", "thriller", "mystery", "print", "file"]
#     query = query.lower()
#     query = " ".join([word for word in query.split() if word not in stop_words])
#     query = re.sub(r"\b(pl(e|i|a)+s(e)?|movie|find|any(one)?|film|link)\b", "", query, flags=re.IGNORECASE)
#     query = re.sub(r"\s+", " ", query).strip()
#     return query

# async def auto_filter(client, message):
#     # query = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else ""

#     if message.text.startswith("/"): return  # ignore commands
#     if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
#         return
#     if len(message.text) < 100:
#         search = message.text
#         try:
#             searchee = normalize_query(message.text)
#             print(searchee)
#         except Exception as e:
#             print(e)
#             pass
#         m = await message.reply_text(f"<b><i> 𝖲𝖾𝖺𝗋𝖼𝗁𝗂𝗇𝗀 𝖿𝗈𝗋 '{search}' 🔎</i></b>")
#         search = search.lower()
#         find = search.split(" ")
#         search = ""
#         removes = ["in","upload", "series", "full", "horror", "thriller", "mystery", "print", "file"]
#         for x in find:
#             if x in removes:
#                 continue
#             else:
#                 search = search + x + " "
#         search = re.sub(r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|bro|bruh|broh|helo|that|find|dubbed|link|venum|iruka|pannunga|pannungga|anuppunga|anupunga|anuppungga|anupungga|film|undo|kitti|kitty|tharu|kittumo|kittum|movie|any(one)|with\ssubtitle(s)?)", "", search, flags=re.IGNORECASE)
#         search = re.sub(r"\s+", " ", search).strip()
#         search = search.replace("-", " ")
#         search = search.replace(":","")
#         print(f"Its search org results : {search}")
#         results = await search_movie(query=search, offset=0, limit=10)
#         await m.delete()

#     else:
#         return

#     if not results:
#         await message.reply_text("No movies found.")
#         return

#     display_text = ""
#     for movie in results:
#         display_text += f"• <a href='{movie['link']}'>{movie['title']}</a>\n\n"

#     buttons = []
#     if len(results) == 10:  # Check if there are more results
#         buttons.append(InlineKeyboardButton("Next ⋟", callback_data=f"next_10_{search}"))

#     reply_markup = InlineKeyboardMarkup([buttons])
#     await message.reply_text(
#         text=f"Search Results:\n\n{display_text}",
#         reply_markup=reply_markup,
#         parse_mode=enums.ParseMode.HTML,
#     )

# @Client.on_callback_query(filters.regex(r"^next_\d+"))
# async def next_page(bot, query):
#     _, offset, search = query.data.split("_")
#     offset = int(offset)

#     limit = 10  # Number of items per page
#     results = await search_movie(query=search, offset=offset, limit=limit)
#     total_movies = await db.total_movies_count()

#     if not results:
#         await query.answer("No more results.")
#         return

#     display_text = ""
#     for movie in results:
#         display_text += f"• <a href='{movie['link']}'>{movie['title']}</a>\n"

#     buttons = []
#     if offset > 0:
#         buttons.append(InlineKeyboardButton("⋞ Back", callback_data=f"next_{offset - limit}_{search}"))
#     if offset + limit < total_movies:
#         buttons.append(InlineKeyboardButton("Next ⋟", callback_data=f"next_{offset + limit}_{search}"))

#     reply_markup = InlineKeyboardMarkup([buttons])
#     await query.edit_message_text(
#         text=f"Search Results:\n\n{display_text}",
#         reply_markup=reply_markup,
#         parse_mode=enums.ParseMode.HTML,
#     )

# # async def next_page(bot, query):
# #     _, offset, search = query.data.split("_")
# #     offset = int(offset)

# #     limit = 10  # Number of items per page
# #     results = await search_movie(query=search, offset=offset, limit=limit)
# #     total_movies = await db.total_movies_count()

# #     if not results:
# #         await query.answer("No more results.")
# #         return

# #     # Format the results into a display text
# #     display_text = ""
# #     for movie in results:
# #         display_text += f"• <a href='{movie['link']}'>{movie['title']}</a>\n"

# #     # Create pagination buttons
# #     buttons = []
# #     if offset > 0:
# #         buttons.append(InlineKeyboardButton("⋞ Back", callback_data=f"next_{offset - limit}_{search}"))
# #     if offset + limit < total_movies:
# #         buttons.append(InlineKeyboardButton("Next ⋟", callback_data=f"next_{offset + limit}_{search}"))

# #     reply_markup = InlineKeyboardMarkup([buttons])
# #     await query.edit_message_text(
# #         text=f"Search Results:\n\n{display_text}",
# #         reply_markup=reply_markup,
# #         parse_mode=enums.ParseMode.HTML,
# #     )


# # async def next_page(bot, query):
# #     _, offset = query.data.split("_")
# #     offset = int(offset)

# #     limit = 10  # Number of items per page
# #     results = await search_movie(query=query.message.text, offset=offset, limit=limit)
# #     total_movies = await db.total_movies_count()

# #     if not results:
# #         await query.answer("No more results.")
# #         return

# #     # Format the results into a display text
# #     display_text = ""
# #     for movie in results:
# #         display_text += f"• <a href='{movie['link']}'>{movie['title']}</a>\n"

# #     # Create pagination buttons
# #     buttons = []
# #     if offset > 0:
# #         buttons.append(InlineKeyboardButton("⋞ Back", callback_data=f"next_{offset - limit}"))
# #     if offset + limit < total_movies:
# #         buttons.append(InlineKeyboardButton("Next ⋟", callback_data=f"next_{offset + limit}"))

# #     reply_markup = InlineKeyboardMarkup([buttons])
# #     await query.edit_message_text(
# #         text=f"Search Results:\n\n{display_text}",
# #         reply_markup=reply_markup,
# #         parse_mode=enums.ParseMode.HTML,
# #     )


# # async def auto_filter(client, msg, spoll=False):
# #     message = msg.message.reply_to_message  # msg will be callback query
# #     search, files, offset, total_results = spoll
# #     m=await message.reply_text(f"<b><i> 𝖲𝖾𝖺𝗋𝖼𝗁𝗂𝗇𝗀 𝖿𝗈𝗋 '{search}' 🔎</i></b>")
# #     await msg.message.delete()

# #     btn = []
# #     if offset != "":
# #         req = message.from_user.id if message.from_user else 0
# #         try:
# #             btn.append(
# #                 [InlineKeyboardButton("𝐏𝐀𝐆𝐄", callback_data="pages"), InlineKeyboardButton(text=f"1/{math.ceil(int(total_results)/int(MAX_BTN))}",callback_data="pages"), InlineKeyboardButton(text="𝐍𝐄𝐗𝐓 ➪",callback_data=f"next_{req}_{key}_{offset}")]
# #             )
# #         except KeyError:
# #             btn.append(
# #                 [InlineKeyboardButton("𝐏𝐀𝐆𝐄", callback_data="pages"), InlineKeyboardButton(text=f"1/{math.ceil(int(total_results)/10)}",callback_data="pages"), InlineKeyboardButton(text="𝐍𝐄𝐗𝐓 ➪",callback_data=f"next_{req}_{key}_{offset}")]
# #             )
# #     else:
# #         btn.append(
# #             [InlineKeyboardButton(text="𝐍𝐎 𝐌𝐎𝐑𝐄 𝐏𝐀𝐆𝐄𝐒",callback_data="pages")]
# #         )

# #     cap = f"<b>😙Rᴇǫᴜᴇsᴛᴇᴅ Bʏ : {message.from_user.mention}\n\n😊 Yᴏᴜʀ Qᴜᴇʀʏ : {search}\n\n📂Tᴏᴛᴀʟ Fɪʟᴇs Fᴏᴜɴᴅᴇᴅ : {total_results}</b>"


# #     fuk = await message.reply_text(text=cap, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
# #     await m.delete()
    
# #     try:
# #         await asyncio.sleep(300)
# #         await fuk.delete()
# #         await message.delete()
# #     except KeyError:
# #         await asyncio.sleep(300)
# #         await fuk.delete()
# #         await message.delete()

