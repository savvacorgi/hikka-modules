# -*- coding: utf-8 -*-

# Импорты для Hikka
from hikkatl.types import Message
from .. import loader, utils

@loader.tds
class PMSSenderMod(loader.Module):
    """Отправка сообщения в ЛС указанному пользователю через команду .pms"""
    strings = {"name": "PMSSender"}

    async def pmscmd(self, message: Message):
        """Использование: .pms <username или ответ на сообщение> <текст сообщения>"""
        args = utils.get_args_raw(message)
        
        # Проверка на наличие аргументов
        if not args:
            await message.edit("<b>Пожалуйста, укажи получателя и сообщение.</b>")
            return
        
        # Если есть ответ на сообщение, берем ID автора
        reply = await message.get_reply_message()
        if reply:
            user_id = reply.sender_id
            text = args
        else:
            # Если нет ответа, пытаемся разобрать аргументы
            args = args.split(" ", 1)
            if len(args) < 2:
                await message.edit("<b>Пожалуйста, укажи получателя и сообщение.</b>")
                return
            user_id = args[0]
            text = args[1]
        
        # Отправка сообщения в ЛС
        try:
            await message.client.send_message(user_id, text)
            await message.edit("<b>Сообщение отправлено!</b>")
        except Exception as e:
            await message.edit(f"<b>Ошибка отправки: {e}</b>")
