import asyncio
import os
from pytz import timezone
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# Muhit o'zgaruvchilaridan o'qiladi (Render uchun)
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
session = os.environ['SESSION']

# O'zbekiston soat zonasi
tz = timezone('Asia/Tashkent')

async def main():
    async with TelegramClient(session, api_id, api_hash) as client:
        while True:
            now = datetime.now(tz).strftime("%H:%M")
            await client(UpdateProfileRequest(
                first_name=f"АбуБакр | {now}",
                last_name=""
            ))
            print(f"Yangilandi: АбуБакр | {now}")
            await asyncio.sleep(45)

asyncio.run(main())

