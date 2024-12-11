from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = '7759131818:AAERSeIcuRc4G9TD8LYV5fmllmDgUjrUEEQ'
# from utils.env import BOT_TOKEN
import logging


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode='html')

dp = Dispatcher(bot, storage=storage)