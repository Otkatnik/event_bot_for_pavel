
import os
from dotenv import load_dotenv
from aiogram import Bot

load_dotenv()
api_key = os.getenv('API_KEY')
admin_chat_id = os.getenv('CHAT_ID_ADMIN')
bot = Bot(token=api_key)
