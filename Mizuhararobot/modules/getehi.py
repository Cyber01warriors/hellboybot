import html
import random
import time

import Mizuhararobot.modules.fun_strings as fun_strings
from Mizuhararobot import dispatcher
from Mizuhararobot.modules.disable import DisableAbleCommandHandler
from Mizuhararobot.modules.helper_funcs.chat_status import is_user_admin
from Mizuhararobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async

EHI_STRINGS = ("Lmao, wait it's on next update")


@run_async
def ehi(update: Update, context: CallbackContext):
    update.effective_message.reply_text(EHI_STRINGS)

EHI_HANDLER = DisableAbleCommandHandler("ehi", ehi)
