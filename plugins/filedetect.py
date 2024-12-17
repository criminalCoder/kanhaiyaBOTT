from pyrogram import Client, filters, enums
# from pyrogram.enums import MessageMediaType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

from pyrogram import Client, filters
import re
import asyncio
from config import *
from lazydeveloper.helpers import AsyncIter, validate_query
# Initialize Pyrogram Client
from telethon import TelegramClient
from telethon.sessions import StringSession


Lazyuserbot = TelegramClient(StringSession(USER_SESSION_STRING), API_ID, API_HASH)
   #   await lazydeveloperrsession.start()


@Client.on_message(filters.group & filters.text & filters.incoming & ~filters.command(['start']))
async def message_handler(client, message):
      try:
         if message.text.startswith("/"):
               return

         print("\nMessage Received: " + message.text)

        # Validate and sanitize query
         args = message.text
         queryz = await validate_query(args)

         if not queryz:
               await message.reply("Please provide a valid search query.")
               return
         # Start Telethon session
         if not Lazyuserbot.is_connected():
            await Lazyuserbot.start()
         # await Lazyuserbot.start()

         print(f"Search Query: {queryz}")
         txt = await message.reply(f"**Searching for links matching:** `{queryz}` 🔍")

      #   Start search logic
         # search_results = []
         # try:
         #    # Search for messages containing the query term in the database channel
         #    async for search_msg in Lazyuserbot.iter_messages(DB_CHANNEL, search=queryz, limit=5):
         #       if search_msg.text:
         #             # Look for a URL in the first line
         #          match = re.match(r"(https?://[^\s]+)", search_msg.text)
         #          if match:
         #             search_results.append(match.group(1))  # Append the URL
         # except Exception as e:
         #       print(f"Error while searching messages: {e}")
         #       await message.reply("An error occurred while searching.")
         #       return
         # Start search logic
         # search_results = []
         # try:
         #    # Search for messages containing the query term in the database channel
         #    async for search_msg in Lazyuserbot.iter_messages(DB_CHANNEL, search=queryz, limit=5):
         #       if search_msg.text:
         #          # Look for a URL in the first line and movie name in the second line
         #          lines = search_msg.text.split("\n")
         #          if len(lines) > 1:
         #                target_url = lines[0].strip()  # The first line is the URL
         #                movie_name = lines[1].strip()  # The second line is the movie name

         #                # Clean movie name by removing parentheses
         #                movie_name = re.sub(r"[()]", "", movie_name)

         #                # Append the formatted result: movie name and URL
         #                search_results.append((movie_name, target_url))
         # except Exception as e:
         #       print(f"Error while searching messages: {e}")
         #       await message.reply("An error occurred while searching.")
         #       return
         search_results = []
         try:
            # Search for messages containing the query term in the database channel
            async for search_msg in Lazyuserbot.iter_messages(DB_CHANNEL, search=queryz, limit=5):
               if search_msg.text:
                     # Look for a URL in the first line
                     match = re.match(r"(https?://[^\s]+)", search_msg.text)
                     if match:
                        target_url = match.group(1).strip()  # Extract the URL
                        
                        # Extract the movie name from text in parentheses ()
                        movie_name_match = re.search(r"\(([^)]+)\)", search_msg.text)
                        movie_name = movie_name_match.group(1).strip() if movie_name_match else "Missing title 😂"
                        
                        # Append the result as a tuple of (movie_name, target_url)
                        search_results.append((movie_name, target_url))
         except Exception as e:
            print(f"Error while searching messages: {e}")
            await message.reply("An error occurred while searching.")
            return
 
        # Handle no results
         if not search_results:
            no_result_text = (
                f"**No results found for '{queryz}'**\n\n"
                f"Try refining your query or checking spelling on "
                f"[Google](http://www.google.com/search?q={queryz.replace(' ', '%20')}%20Movie) 🔍."
            )
            await txt.delete()
            await message.reply(no_result_text, disable_web_page_preview=True)
            return

         # Generate and send result message
         #   result_message = "\n\n".join(
         #       [
         #           f"✅ **Result {i + 1}:**\n{search_msg.text or 'Media/Caption Message'}"
         #           for i, search_msg in enumerate(search_results)
         #       ]
         #   )
         # result_message = "\n\n".join(
         #       [
         #          f"✅ **Result {i + 1}:**\n[{match.group(2)}]({match.group(1)})"
         #          for i, search_msg in enumerate(search_results)
         #          if (match := re.match(r"(https?://[^\s]+) \((.+?)\)", search_msg.text))
         #       ]
         #    )
         # result_message = "\n\n".join([f"✅ **Result {i + 1}:**\n{url}" for i, url in enumerate(search_results)])
         result_message = "\n\n".join([f"<blockquote>🎥 <b>{movie_name}</b>\n<b>Link:</b> {target_url}</blockquote>" for movie_name, target_url in search_results])
         print('got result')
         response = (
            f"**Search Results for '{queryz}':**\n\n"
            f"{result_message}\n\n"
         )

         await txt.delete()
         result = await message.reply(response, disable_web_page_preview=True)

         # Auto-delete results after a delay
         await asyncio.sleep(AUTO_DELETE_TIME)
         await result.delete()

      except Exception as e:
         print(e)
         if txt:
               await txt.delete()
         await message.reply("I couldn't process your request. Please try again later.")
      finally:
         await asyncio.sleep(1)
         await Lazyuserbot.disconnect()
         if not Lazyuserbot.is_connected():
               print("Session is disconnected successfully!")
         else:
               print("Session is still connected.")
               await Lazyuserbot.disconnect()
               print("Tried to disconnect session.")
         return

