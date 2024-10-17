# -*- coding: utf-8 -*-

import os
from .. import loader
from hikkatl.types import Message

@loader.tds
class ServerStatsMod(loader.Module):
    strings = {"name": "ServerStats"}

    async def sysinfocmd(self, message: Message):
        total_ram = os.popen('free -m | awk \'/^Mem:/ {print $2}\'').read().strip()
        used_ram = os.popen('free -m | awk \'/^Mem:/ {print $3}\'').read().strip()
        free_ram = os.popen('free -m | awk \'/^Mem:/ {print $4}\'').read().strip()
        cpu_info = os.popen('top -bn1 | grep "Cpu(s)"').read().strip()
        total_disk = os.popen('df -h / | awk \'/\// {print $2}\'').read().strip()
        used_disk = os.popen('df -h / | awk \'/\// {print $3}\'').read().strip()
        free_disk = os.popen('df -h / | awk \'/\// {print $4}\'').read().strip()

        info = (
            f"<b>Системная информация:</b>\n"
            f"Общая оперативная память: {total_ram} МБ\n"
            f"Использовано оперативной памяти: {used_ram} МБ\n"
            f"Свободно оперативной памяти: {free_ram} МБ\n"
            f"Загрузка CPU: {cpu_info.split(',')[0].split()[1]}%\n\n"
            f"<b>Диск:</b>\n"
            f"Всего: {total_disk}\n"
            f"Использовано: {used_disk}\n"
            f"Свободно: {free_disk}\n"
        )

        await message.edit(info)
