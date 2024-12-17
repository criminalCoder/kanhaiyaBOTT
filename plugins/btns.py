# import math
# from pyrogram import Client, filters, enums
# from pyrogram.errors import MessageNotModified
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# MOVIE_DATABASE = -1001234567890  # Replace with your database channel ID
# MAX_BTN = 10  # Number of results per page

# user_files_data = {}  # Cache for user-specific files


# @Client.on_message(filters.command("search"))
# async def search_movies(client, message):
#     """
#     Command to search for movies in the database channel.
#     """
#     query = message.text.split(" ", 1)
#     if len(query) < 2:
#         await message.reply_text("❌ Please provide a movie name to search!")
#         return

#     movie_name = query[1].strip().lower()
#     user_id = message.from_user.id

#     # Search in the database channel
#     files = []
#     async for msg in client.search_messages(MOVIE_DATABASE, query=movie_name):
#         if movie_name in msg.text.lower():
#             files.append(msg.text)  # Cache message text containing links

#     if not files:
#         await message.reply_text("❌ No results found for your query.")
#         return

#     # Cache the user's search results
#     user_files_data[user_id] = files

#     # Display the first page
#     await display_files(message, user_id, offset=0)


# async def display_files(message, user_id, offset):
#     """
#     Display a page of search results with navigation buttons.
#     """
#     files_data = user_files_data.get(user_id, [])
#     total_results = len(files_data)

#     # Slice files for the current page
#     files = files_data[offset:offset + MAX_BTN]
#     next_offset = offset + MAX_BTN if offset + MAX_BTN < total_results else None
#     prev_offset = offset - MAX_BTN if offset > 0 else None

#     # Build the display text
#     display_text = ""
#     for file in files:
#         # Extract movie title and link from the text
#         try:
#             title, link = file.split("\n")[0], file.split("\n")[1]  # Assuming a standard format
#         except IndexError:
#             continue  # Skip malformed entries
#         display_text += f"• <a href='{link}'>{title}</a>\n⍟───────────────────\n"

#     # Build navigation buttons
#     btn = []
#     if prev_offset is not None:
#         btn.append(InlineKeyboardButton("⋞ ʙᴀᴄᴋ", callback_data=f"prev_{prev_offset}"))
#     if next_offset is not None:
#         btn.append(InlineKeyboardButton("ɴᴇxᴛ ⋟", callback_data=f"next_{next_offset}"))
#     if btn:
#         btn = [btn]
#     btn.append([InlineKeyboardButton(f"🗓 {offset // MAX_BTN + 1}/{math.ceil(total_results / MAX_BTN)}", callback_data="pages")])

#     # Send or edit the message
#     try:
#         await message.reply_text(
#             f"<b>🔍 Search Results:</b>\n{display_text}",
#             reply_markup=InlineKeyboardMarkup(btn),
#             parse_mode=enums.ParseMode.HTML,
#             disable_web_page_preview=True
#         )
#     except Exception as e:
#         await message.reply_text(f"❌ Error displaying files: {e}")


# @Client.on_callback_query(filters.regex(r"^next"))
# async def next_page(client, query):
#     """
#     Handle 'Next' button to show the next page of results.
#     """
#     offset = int(query.data.split("_")[1])
#     user_id = query.from_user.id
#     await query.answer()
#     await display_files(query.message, user_id, offset)


# @Client.on_callback_query(filters.regex(r"^prev"))
# async def prev_page(client, query):
#     """
#     Handle 'Previous' button to show the previous page of results.
#     """
#     offset = int(query.data.split("_")[1])
#     user_id = query.from_user.id
#     await query.answer()
#     await display_files(query.message, user_id, offset)
