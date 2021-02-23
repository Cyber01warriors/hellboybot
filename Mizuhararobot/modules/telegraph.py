import os

from pyrogram import filters
from telegraph import upload_file
from Mizuhararobot import pbot as app


@app.on_message(filters.command('telegraph')
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply(message, text='reply to a supported media file')
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith('.mp4')
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                ('.jpg', '.jpeg', '.png', '.gif', '.mp4'),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply(message, text='not supported!')
        return
    download_location = await client.download_media(
        message=message.reply_to_message, file_name='root/mizuki/',
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            message,
            text=f'**Uploaded to Telegraph by @TheMizukiBot\n\n👉 https://telegra.ph{response[0]}**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
