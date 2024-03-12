import asyncio
import handlers
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from db import create_user_table
from config import read_config
from logger_config import configure_logging


async def main():
    config = read_config('settings.ini')
    await create_user_table()
    # Инициализация бота
    botS = Bot(token=config["Tg"]["api_bot"], parse_mode='HTML')
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(handlers.router)

    await botS.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(botS)


# Запуск бота
if __name__ == '__main__':
    configure_logging()
    asyncio.run(main())
