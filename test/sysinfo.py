# -*- coding: utf-8 -*-

import os
import platform
from .. import loader
from hikkatl.types import Message

@loader.tds
class ServerStatsMod(loader.Module):
    strings = {"name": "ServerStats"}

    async def sysinfocmd(self, message: Message):
        uname = platform.uname()
        
        total_ram = os.popen('cat /proc/meminfo | grep MemTotal').read().strip().split()[1]
        used_ram = os.popen('cat /proc/meminfo | grep MemAvailable').read().strip().split()[1]
        total_disk = os.popen('df -h / | awk \'\$1 == "Filesystem" {print $2}\'').read().strip()
        used_disk = os.popen('df -h / | awk \'\$1 == "Filesystem" {print $3}\'').read().strip()
        free_disk = os.popen('df -h / | awk \'\$1 == "Filesystem" {print $4}\'').read().strip()

        info = (
            f"<b>Системная информация:</b>\n"
            f"OS: {uname.system} {uname.release}\n"
            f"Архитектура: {uname.machine}\n"
            f"Процессор: {uname.processor}\n\n"
            f"<b>Оперативная память:</b>\n"
            f"Всего RAM: {int(total_ram) / 1024:.2f} МБ\n"
            f"Использовано RAM: {int(used_ram) / 1024:.2f} МБ\n\n"
            f"<b>Диск:</b>\n"
            f"Всего: {total_disk}\n"
            f"Использовано: {used_disk}\n"
            f"Свободно: {free_disk}\n"
        )

        await message.edit(info)
