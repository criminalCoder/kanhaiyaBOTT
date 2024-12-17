
import re
from config import *
import json
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lazydeveloper.lazydb import db
import requests

import re
async def validate_query(q):
    query = q
            # Checking if the length of the query is less than 2. If it is, it returns.
    if len(query) < 2:
        return False
   
    # Checking if the message contains any of the following:
    #         1. /
    #         2. ,
    #         3. .
    #         4. Emojis
    #         If it does, it will return.
    if re.findall(r"((^\/|^,|^:|^\.|^[\U0001F600-\U000E007F]).*)", query):
        return False
    
    # Checking if the message contains a link.
    if ("https://" or "http://") in query:
        return False

    # It removes the year from the search query.|hello|file|that|find|und(o)*|kit(t(i|y)?)?o(w)?|kitt
    query = re.sub(r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|gib)(\sme)?)|new|hd|\(|\)|dedo|print|fulllatest|br((o|u)h?)*um(o)*|aya((um(o)*)?|any(one)|with\ssk)*ubtitle(s)?)", "", query.lower(), flags=re.IGNORECASE)
    return query.strip()


class AsyncIter:    
    def __init__(self, items):    
        self.items = items    

    async def __aiter__(self):    
        for item in self.items:    
            yield item  