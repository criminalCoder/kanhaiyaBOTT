from os import link
from telethon import Button
from config import *
from pyrogram import Client, idle
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

from telethon import TelegramClient, events
import urllib.parse
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
import re
tbot = TelegramClient('mdisktelethonbot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
client = TelegramClient(StringSession(USER_SESSION_STRING), API_ID, API_HASH)

from lazydeveloper.helpers import validate_query, AsyncIter


@tbot.on(events.NewMessage(incoming=True))
async def message_handler(event):
    try:
        if event.message.post:
            return

        # if event.is_channel:return
        if event.text.startswith("/"):return

        print("\n")
        print("Message Received: " + event.text)

        # Force Subscription


        args = event.text
        queryz = await validate_query(args)

        print(f"Search Query: {args}".format(args=queryz))
        print("\n")

        if not queryz:
            return

        txt = await event.reply('**Printing Links For "{}" 🔍**'.format(event.text))


        # put the search logic here :

        # Search logic using Telethon's `iter_messages`
        search_results = []
        try:
            async for search_term in AsyncIter(re.sub("__|\*", "", args).split()):
                if len(search_term) > 2:
                    search_msg = client.iter_messages(DB_CHANNEL, limit=5, search=search_term)
                    search_results.append(search_msg)
        except Exception as e:
            print(f"Error while searching messages: {e}")

        # If no results found
        if not search_results:
            no_result_text = (
                f"**Sorry, no results found for '{queryz}'**\n\n"
                f"Try refining your query or check spelling on "
                f"[Google](http://www.google.com/search?q={queryz.replace(' ', '%20')}%20Movie) 🔍."
            )
            # await response_msg.delete()
            await event.reply(no_result_text)
            return
        
        # Generate result message
        result_message = "\n\n".join(
            [f"✅ **Result {i + 1}:**\n{result}" for i, result in enumerate(search_results)]
        )

        message = (
            f"**Search Results for '{queryz}':**\n\n"
            f"{result_message}\n\n"
        )

        await txt.delete()
        await asyncio.sleep(0.5)
        result = await event.reply(message, link_preview=False)
        await asyncio.sleep(AUTO_DELETE_TIME)
        # await event.delete()
        return await result.delete()

    except Exception as e:
        print(e)
        await txt.delete()
        result = await event.reply("I am Unable Search")
        await asyncio.sleep(AUTO_DELETE_TIME)
        await event.delete() 
        return await result.delete()


# async def escape_url(str):
#     escape_url = urllib.parse.quote(str)
#     return escape_url

# Bot Client for Inline Search
Bot = Client(
    session_name=BOT_SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

print()
print("-------------------- Initializing Telegram Bot --------------------")
# Start Clients
Bot.start()

print("------------------------------------------------------------------")
print()
print(f"""
 _____________________________________________   
|                                             |  
|          Deployed Successfully              |  
|              Join @LazyDeveloper            |
|_____________________________________________|
    """)

# User.start()
with tbot, client:
    tbot.run_until_disconnected()
    client.run_until_disconnected()

# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
print()
print("------------------------ Stopped Services ------------------------")
Bot.stop()
# User.stop()
