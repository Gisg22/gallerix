from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from parsing.scraping import get_href
from aiogram.dispatcher import Dispatcher

choice = InlineKeyboardMarkup(row_width=1)
hrefs = get_href()

leonardo_kb = InlineKeyboardButton(
    text='Леонардо да Винчи',
    url=hrefs[0]
)

choice.insert(leonardo_kb)

rembrant_kb = InlineKeyboardButton(
    text='Рембрандт',
    url=hrefs[1]
)
choice.insert(rembrant_kb)

van_gog_kb = InlineKeyboardButton(
    text='Ван Гог',
    url=hrefs[2]
)
choice.insert(van_gog_kb)

rafael_kb = InlineKeyboardButton(
    text='Рафаэль',
    url=hrefs[3]
)
choice.insert(leonardo_kb)

tician_kb = InlineKeyboardButton(
    text='Тициан',
    url=hrefs[4]
)
choice.insert(tician_kb)

michelangelo_kb = InlineKeyboardButton(
    text='Микеланджело',
    url=hrefs[5]
)

choice.insert(michelangelo_kb)

kavaragio_kb = InlineKeyboardButton(
    text='Караваджо',
    url=hrefs[6]
)
choice.insert(kavaragio_kb)

bottichelli_kb = InlineKeyboardButton(
    text='Боттичелли',
    url=hrefs[7]
)
choice.insert(bottichelli_kb)

bosh_kb = InlineKeyboardButton(
    text='Босх',
    url=hrefs[8]
)
choice.insert(bosh_kb)
velaskes_kb = InlineKeyboardButton(
    text='Веласкес',
    url=hrefs[9]
)

choice.insert(leonardo_kb)

rubens_kb = InlineKeyboardButton(
    text='Рубенс',
    url=hrefs[10]
)
choice.insert(rubens_kb)

klimt_kb = InlineKeyboardButton(
    text='Климт',
    url=hrefs[11]
)
choice.insert(klimt_kb)

bermeer_kb = InlineKeyboardButton(
    text='Вермеер',
    url=hrefs[12]
)

choice.insert(bermeer_kb)
aivazovski_kb = InlineKeyboardButton(
    text='Айвазовский',
    url=hrefs[13]
)

choice.insert(aivazovski_kb)

shishkin_kb = InlineKeyboardButton(
    text='Шишкин',
    url=hrefs[14]
)

choice.insert(shishkin_kb)


async def url_command(message: Message):
    await message.answer('Выберите автора и вы перейдете по ссылке', reply_markup=choice)


def register_inline_handlers(dp: Dispatcher):
    dp.register_message_handler(url_command, commands=['pic'])
