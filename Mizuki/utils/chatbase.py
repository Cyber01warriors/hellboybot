# the logging things
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from Mizuki import CHAT_BASE_TOKEN
else:
    from Mizuki import CHAT_BASE_TOKEN

# the Strings used for this "thing"


# the Telegram trackings
from chatbase import Message


def TRChatBase(chat_id, message_text, intent):
    msg = Message(
        api_key=CHAT_BASE_TOKEN,
        platform="Telegram",
        version="1.3",
        user_id=chat_id,
        message=message_text,
        intent=intent,
    )
    msg.send()
