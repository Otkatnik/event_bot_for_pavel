import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router
from config import bot  # импортируем bot из config.py
from aiogram.fsm.storage.memory import MemoryStorage


load_dotenv()
api_key = os.getenv('API_KEY')
admin_chat_id = os.getenv('CHAT_ID_ADMIN')
dp = Dispatcher()
storage = MemoryStorage()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
