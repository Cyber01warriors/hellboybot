from typing import Callable, Dict, List, Union

from pyrogram import Client
from pyrogram.types import Chat, Message, User

from Mizuki import OWNER_ID

admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get(chat_id: int) -> Union[List[int], bool]:
    if chat_id in admins:
        return admins[chat_id]

    return False


async def get_administrators(chat: Chat) -> List[User]:
    get = admins.get(chat.id)

    if get:
        return get
    else:
        administrators = await chat.get_members(filter="administrators")
        to_set = []

        for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        admins.set(chat.id, to_set)
        return await get_administrators(chat)


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in OWNER_ID:
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator
