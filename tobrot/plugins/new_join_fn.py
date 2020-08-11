#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


from tobrot.amocmadin import Loilacaztion


async def new_join_f(client, message):
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)
    # reply the correct CHAT ID,
    # and LEAVE the chat
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            Loilacaztion.WRONG_MESSAGE.format(
                CHAT_ID=message.chat.id
            )
        )
        # leave chat
        await message.chat.leave()


async def help_message_f(client, message):
    pass
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    # channel_id = str(AUTH_CHANNEL)[4:]
    # message_id = 99
    # display the /help message
    # await message.reply_text(
    #    f"please read the <a href='https://t.me/c/{channel_id}/{message_id}'>Pinned Message</a>",
    #    quote=True
    # )
