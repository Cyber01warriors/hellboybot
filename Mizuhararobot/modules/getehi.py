import html
import random
import time
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode,
                      Update)
import Mizuhararobot.modules.fun_strings as fun_strings
from Mizuhararobot import dispatcher
from Mizuhararobot.modules.disable import DisableAbleCommandHandler
from Mizuhararobot.modules.helper_funcs.chat_status import is_user_admin
from Mizuhararobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async

EHI_STRINGS = ("Here, latest ehi files by @TheMizukiBot 👸",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="👉 Download EHI Files 👈",
                            url="https://www.mediafire.com/folder/1g0te1sz25qrt/Mizuki+EHI")
                    ]]))


@run_async
def ehi(update: Update, context: CallbackContext):
    update.effective_message.reply_text(EHI_STRINGS)

EHI_HANDLER = DisableAbleCommandHandler("ehi", ehi)
dispatcher.add_handler(EHI_HANDLER)
