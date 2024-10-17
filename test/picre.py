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
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.text()
                    # Извлечение изображения из HTML (предполагается, что картинка в теге <img>)
                    img_url = self.extract_image_url(data)
                    if img_url:
                        await message.reply(img_url)
                    else:
                        await message.reply("Не удалось найти изображение.")
                else:
                    await message.reply("Ошибка при получении изображения.")

    def extract_image_url(self, html):
        import re
        match = re.search(r'<img src="(.*?)"', html)
        return match.group(1) if match else None
