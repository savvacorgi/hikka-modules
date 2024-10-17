# -*- coding: utf-8 -*-

from hikkatl.types import Message
from .. import loader, utils

@loader.tds
class PMSSenderMod(loader.Module):
    strings = {"name": "PMSSender"}

    async def pmscmd(self, message: Message):
        args = utils.get_args_raw(message)
        
        if not args:
            await message.edit("<b>Пожалуйста, укажи получателя и сообщение.</b>")
            return
        
        reply = await message.get_reply_message()
        if reply:
            user_id = reply.sender_id
            text = args
        else:
            args = args.split(" ", 1)
            if len(args) < 2:
                await message.edit("<b>Пожалуйста, укажи получателя и сообщение.</b>")
                return
            user_id = args[0]
            text = args[1]
        
        try:
            await message.client.send_message(user_id, text)
            await message.delete()
        except Exception as e:
            await message.edit(f"<b>Ошибка отправки: {e}</b>")

    async def grcmd(self, message: Message):
        args = utils.get_args_raw(message)
        
        if not args:
            await message.edit("<b>Пожалуйста, укажи группу и сообщение.</b>")
            return

        args = args.split(" ", 1)
        if len(args) < 2:
            await message.edit("<b>Пожалуйста, укажи группу и сообщение.</b>")
            return
        group = args[0]
        text = args[1]
        
        try:
            await message.client.send_message(group, text)
            await message.delete()
        except Exception as e:
            await message.edit(f"<b>Ошибка отправки: {e}</b>")
