# the logging things
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import os
import shutil
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from Mizuki import DEF_WATER_MARK_FILE, DOWNLOAD_LOCATION
else:
    from Mizuki import DEF_WATER_MARK_FILE, DOWNLOAD_LOCATION

# the Strings used for this "thing"
import pyrogram

from Mizuki.utils.anydl_trans import Translation

logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InputMediaPhoto

from Mizuki import pbot as bot
from Mizuki.utils.chatbase import TRChatBase
from Mizuki.utils.display_progress import progress_for_pyrogram
from Mizuki.utils.help_Nekmo_ffmpeg import generate_screen_shots


@bot.on_message(pyrogram.filters.command(["genss"]))
async def generate_screen_shot(bot, update):
    TRChatBase(update.from_user.id, update.text, "generatescss")
    if update.reply_to_message is not None:
        download_location = DOWNLOAD_LOCATION + "/"
        a = await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_START,
            reply_to_message_id=update.message_id,
        )
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=update.reply_to_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(Translation.DOWNLOAD_START, a, c_time),
        )
        if the_real_download_location is not None:
            await bot.edit_message_text(
                text=Translation.SAVED_RECVD_DOC_FILE,
                chat_id=update.chat.id,
                message_id=a.message_id,
            )
            tmp_directory_for_each_user = (
                DOWNLOAD_LOCATION + "/" + str(update.from_user.id)
            )
            if not os.path.isdir(tmp_directory_for_each_user):
                os.makedirs(tmp_directory_for_each_user)
            images = await generate_screen_shots(
                the_real_download_location,
                tmp_directory_for_each_user,
                False,
                DEF_WATER_MARK_FILE,
                5,
                9,
            )
            logger.info(images)
            await bot.edit_message_text(
                text=Translation.UPLOAD_START,
                chat_id=update.chat.id,
                message_id=a.message_id,
            )
            media_album_p = []
            if images is not None:
                i = 0
                caption = "© @TheMizukiBot"
                for image in images:
                    if os.path.exists(image):
                        if i == 0:
                            media_album_p.append(
                                InputMediaPhoto(
                                    media=image, caption=caption, parse_mode="html"
                                )
                            )
                        else:
                            media_album_p.append(InputMediaPhoto(media=image))
                        i = i + 1
            await bot.send_media_group(
                chat_id=update.chat.id,
                disable_notification=True,
                reply_to_message_id=a.message_id,
                media=media_album_p,
            )
            #
            try:
                shutil.rmtree(tmp_directory_for_each_user)
                os.remove(the_real_download_location)
            except:
                pass
            await bot.edit_message_text(
                text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                chat_id=update.chat.id,
                message_id=a.message_id,
                disable_web_page_preview=True,
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.REPLY_TO_DOC_FOR_SCSS,
            reply_to_message_id=update.message_id,
        )
