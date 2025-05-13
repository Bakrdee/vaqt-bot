from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from pytz import timezone
from datetime import datetime
import time

api_id = 28281539
api_hash = 'ca47bc35c67929f9a3a81aeaa20decfe'
phone_number = '+998930015305'

# O'zbekiston soat zonasi
tz = timezone('Asia/Tashkent')

# Telegram sessiyasini ishga tushirish
with TelegramClient('abubakr', api_id, api_hash) as client:
    client.start(phone=phone_number)

    while True:
        now = datetime.now(tz).strftime("%H:%M")
        client(UpdateProfileRequest(
            first_name=f"АбуБакр | {now}",  # Nik + vaqt
            last_name=""
        ))
        print(f"Yangilandi: АбуБакр | {now}")
        time.sleep(45)  # 45 soniyada yangilanadi
