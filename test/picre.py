# -*- coding: utf-8 -*-

import aiohttp
from .. import loader
from hikkatl.types import Message

@loader.tds
class RimMod(loader.Module):
    strings = {"name": "Rim"}

    async def rimcmd(self, message: Message):
        url = "https://pic.re/image"

        async with aiohttp.ClientSession() as session:
            async with session.post(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    img_url = data.get("file_url")
                    if img_url:
                        await message.client.send_photo(message.chat.id, img_url)  # Отправляем изображение
                    else:
                        await message.reply("Не удалось найти изображение.")
                else:
                    await message.reply("Ошибка при получении изображения.")
