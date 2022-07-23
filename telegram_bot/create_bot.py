from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
