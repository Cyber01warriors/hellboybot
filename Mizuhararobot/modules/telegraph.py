import os
import logging
from PIL import Image
from telethon import TelegramClient, events, Button
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telegraph import Telegraph, exceptions, upload_file
from Mizuhararobot import telethn as bot

@bot.on(events.NewMessage(pattern='/telegraph'))
async def uploader(event):
    TMP_DOWNLOAD_DIRECTORY = "./Downloads/"
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    pic = event.media
    ok = await event.reply("`Downloading...`")
    downloaded_file_name = await bot.download_media(pic, TMP_DOWNLOAD_DIRECTORY)
    try:
        os.remove(downloaded_file_name)
        await ok.edit(f"Uploaded to Telegraph\n\n👉 https://telegra.ph{}")\n\n~ @TheMizukiBot".format(media_urls[0])
