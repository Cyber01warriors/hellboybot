import os

from pyrogram import filters
from urllib.parse import urlparse
from Mizuki import pbot as app
from Mizuki.utils.fetch import fetch

ARQ = "https://thearq.tech/"


@app.on_message(filters.command("deezer"))
async def deezer(_, message):
    if len(message.command) < 2:
        await message.reply_text("/deezer requires an argument.")
        return
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching the song by @Infinity_BOTs 🤗")
    try:
        r = await fetch(f"{ARQ}deezer?query={query}&count=1")
        title = r[0]["title"]
        url = r[0]["url"]
        artist = r[0]["artist"]
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Downloading 😁")
    song = await download_song(url)
    await m.edit("Uploading, Plz wait 😍")
    await message.reply_audio(audio=song, title=title, performer=artist)
    os.remove(song)
    await m.delete()
