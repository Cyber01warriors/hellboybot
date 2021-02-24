import html
import random
import time
import Mizuki.modules.fun_strings as fun_strings
from Mizuki import dispatcher
from Mizuki.modules.disable import DisableAbleCommandHandler
from Mizuki.modules.helper_funcs.chat_status import is_user_admin
from Mizuki.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async

EHI_STRINGS = ("Here, latest ehi files by @TheMizukiBot 👸\n\n👉 https://da.gd/pKZZ")

@run_async
def ehi(update: Update, context: CallbackContext):
    update.effective_message.reply_text(EHI_STRINGS)

EHI_HANDLER = DisableAbleCommandHandler("ehi", ehi)
dispatcher.add_handler(EHI_HANDLER)
