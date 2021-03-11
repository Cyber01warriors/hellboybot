#    Copyright (c) 2021 Infinity BOTs <https://t.me/Infinity_BOTs>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.


import os
import re
import requests
import time
import wget
from pyrogram import filters, types
from pyrogram.types import Message
import speedtest
import psutil
from Mizuki import pbot as app


@app.on_message(filters.command("saavn"))
async def saavn(_, message: Message):
    if len(message.command) < 2:
        await message.reply_text("/saavn requires an argument.")
        return
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching, Plz Wait...\n\n~ @Infinity_BOTs")
    try:
        r = requests.get(f"https://snobybuddymusic.herokuapp.com/result/?query={query}")
    except Exception as e:
        await m.edit(str(e))
        return
    sname = r.json()[0]['song']
    slink = r.json()[0]['media_url']
    ssingers = r.json()[0]['singers']
    file = wget.download(slink)
    ffile = file.replace("mp4", "m4a")
    os.rename(file, ffile)
    await message.reply_audio(audio=ffile, title=sname,
                              performer=ssingers)
    os.remove(ffile)
    await m.delete()
