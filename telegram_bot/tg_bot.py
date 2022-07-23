from aiogram.utils import executor
from create_bot import dp
from headers import others
from inline import inline_buttons

others.register_other_handler(dp)
inline_buttons.register_inline_handlers(dp)


async def on_startup(_):
    print('Бот запущен')


executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
