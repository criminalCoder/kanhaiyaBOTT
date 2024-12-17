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

        # Start search logic
         search_results = []
         try:
            async for search_term in AsyncIter(re.sub("__|\*", "", args).split()):
               if len(search_term) > 2:
                  async for search_msg in Lazyuserbot.iter_messages(DB_CHANNEL, limit=5, search=search_term):
                     if search_msg.text:
                        search_results.append(search_msg.text)
         except Exception as e:
            print(f"Error while searching messages: {e}")
            await txt.delete()
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
         result_message = "\n\n".join(
               [
                  f"✅ **Result {i + 1}:**\n[{match.group(2)}]({match.group(1)})"
                  for i, search_msg in enumerate(search_results)
                  if (match := re.match(r"(https?://[^\s]+) \((.+?)\)", search_msg.text))
               ]
            )
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

