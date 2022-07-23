from aiogram.types import Message
from aiogram.dispatcher import Dispatcher


async def start_bot(message: Message):
    await message.answer('Введите команду /pic для выбора автора')


def register_other_handler(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'])
