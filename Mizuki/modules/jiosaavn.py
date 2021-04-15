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

import requests
import wget
from pyrogram import filters

from Mizuki import pbot as Jebot
from Mizuki.utils.ut import get_arg


@Jebot.on_message(filters.command("saavn"))
async def song(client, message):
    message.chat.id
    message.from_user["id"]
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("<b>What is the song you want?</b>")
        return ""
    m = await message.reply_text("Downloading...")
    try:
        r = requests.get(
            f"https://jevcplayerbot-saavndl.herokuapp.com/result/?query={args}"
        )
    except Exception as e:
        await m.edit(str(e))
        return
    sname = r.json()[0]["song"]
    slink = r.json()[0]["media_url"]
    ssingers = r.json()[0]["singers"]
    file = wget.download(slink)
    ffile = file.replace("mp4", "m4a")
    os.rename(file, ffile)
    await m.edit("Uploading...")
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers)
    os.remove(ffile)
    await m.delete()
