from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram.ext import CommandHandler, run_async, Filters
from Mizuhararobot import dispatcher
from Mizuhararobot.modules.disable import DisableAbleCommandHandler
from Mizuhararobot.modules.helper_funcs.filters import CustomFilters

@run_async
def echo(bot: Bot, update: Update):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(args[1])
    else:
        message.reply_text(args[1], quote=False)
    message.delete()

SEND_HANDLER = CommandHandler("send", echo)
dispatcher.add_handler(SEND_HANDLER)
