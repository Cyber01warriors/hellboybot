# Credits for thehamkercat's Willam Butcher Bot

import time

from pyrogram import filters

from Mizuki import pbot
from Mizuki.utils.fetch import fetch


@pbot.on_message(filters.command("webss"))
async def take_ss(_, message):
    if len(message.command) != 2:
        await message.reply_text("Give A Url To Fetch Screenshot.")
        return
    url = message.text.split(None, 1)[1]
    start_time = time.time()
    m = await message.reply_text("**Taking Screenshot...**")
    screenshot = await fetch(f"https://patheticprogrammers.cf/ss?site={url}")
    await m.edit("**Uploading...**")
    end_time = time.time()
    await pbot.send_photo(
        message.chat.id,
        photo=screenshot,
        caption=(f"{url}\n__Took {round(end_time - start_time)} Seconds.__"),
    )
    await m.delete()
