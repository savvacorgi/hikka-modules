# -*- coding: utf-8 -*-

import psutil
import platform
from .. import loader
from hikkatl.types import Message

@loader.tds
class ServerStatsMod(loader.Module):
    strings = {"name": "ServerStats"}

    async def sysinfocmd(self, message: Message):
        uname = platform.uname()
        cpu_count = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq().current
        cpu_usage = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        total_ram = mem.total / (1024 ** 3)
        used_ram = mem.used / (1024 ** 3)
        free_ram = mem.available / (1024 ** 3)
        disk = psutil.disk_usage('/')
        total_disk = disk.total / (1024 ** 3)
        used_disk = disk.used / (1024 ** 3)
        free_disk = disk.free / (1024 ** 3)

        info = (
            f"<b>Системная информация:</b>\n"
            f"OS: {uname.system} {uname.release}\n"
            f"CPU: {uname.processor} ({cpu_count} ядер)\n"
            f"Частота CPU: {cpu_freq:.2f} MHz\n"
            f"Загрузка CPU: {cpu_usage}%\n\n"
            f"<b>Оперативная память:</b>\n"
            f"Всего RAM: {total_ram:.2f} ГБ\n"
            f"Использовано RAM: {used_ram:.2f} ГБ\n"
            f"Свободно RAM: {free_ram:.2f} ГБ\n\n"
            f"<b>Диск:</b>\n"
            f"Всего: {total_disk:.2f} ГБ\n"
            f"Использовано: {used_disk:.2f} ГБ\n"
            f"Свободно: {free_disk:.2f} ГБ\n"
        )

        await message.edit(info)
