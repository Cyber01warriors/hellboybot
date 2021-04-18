import aiohttp
from pyrogram import filters

from Mizuki import pbot


@pbot.on_message(filters.command("memes"))
async def memes(client, message):
    async with aiohttp.ClientSession() as ses:
        async with ses.get("https://meme-api.herokuapp.com/gimme/wholesomememes") as resp:
            r = await resp.json()
            await message.reply_photo(r["url"], caption=r["title"])


__help__ = """
*Mizuki gives you memes randomly gained through meme API*

• `/memes`*:* get very interesting and funny memes randomly.
"""

__mod_name__ = "Memes"
