# Ported from https://github.com/thehamkercat/WilliamButcherBot

import os
from pyrogram import filters
from pyrogram.types import ChatPermissions
from Mizuki import DRAGONS as SUDOERS
from Mizuki import pbot as app, BOT_ID
from Mizuki.utils.errors import capture_err
import asyncio

async def list_admins(group_id):
    list_of_admins = []
    async for member in app.iter_chat_members(
            group_id, filter="administrators"):
        list_of_admins.append(member.user.id)
    return list_of_admins


async def member_permissions(chat_id, user_id):
    perms = []
    member = (await app.get_chat_member(chat_id, user_id))
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms


@app.on_message(filters.command("set_chat_title") & ~filters.private)
@capture_err
async def set_chat_title(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("You Don't Have Enough Permissions.")
            return
        if len(message.command) < 2:
            await message.reply_text("**Usage:**\n/set_chat_title NEW NAME")
            return
        old_title = message.chat.title
        new_title = message.text.split(None ,1)[1]
        await message.chat.set_title(new_title)
        await message.reply_text(f"Successfully Changed Group Title From {old_title} To {new_title}")
    except Exception as e:
        print(e)
        await message.reply_text(e)


@app.on_message(filters.command("set_user_title") & ~filters.private)
@capture_err
async def set_user_title(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        from_user = message.reply_to_message.from_user
        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("You Don't Have Enough Permissions.")
            return
        if len(message.command) < 2:
            await message.reply_text("**Usage:**\n/set_user_title NEW ADMINISTRATOR TITLE")
            return
        title = message.text.split(None ,1)[1]
        await app.set_administrator_title(chat_id, from_user.id, title)
        await message.reply_text(f"Successfully Changed {from_user.mention}'s Admin Title To {title}")
    except Exception as e:
        print(e)
        await message.reply_text(e)


@app.on_message(filters.command("set_chat_photo") & ~filters.private)
@capture_err
async def set_chat_photo(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("You Don't Have Enough Permissions.")
            return
        if not message.reply_to_message:
            await message.reply_text("Reply to a photo to set it as chat_photo")
            return
        if not message.reply_to_message.photo and not message.reply_to_message.document:
            await message.reply_text("Reply to a photo to set it as chat_photo")
            return
        photo = await message.reply_to_message.download()
        await message.chat.set_photo(photo)
        await message.reply_text("Successfully Changed Group Photo.")
        os.remove(photo)
    except Exception as e:
        print(e)
        await message.reply_text(e)
