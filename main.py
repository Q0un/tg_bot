import logging
import asyncio
from os import environ
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = environ["TOKEN"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class States(StatesGroup):
    no_command = State()
    randint = State()
    random = State()
    calc = State()


async def on_startup(x):
    from handlers import choose_lucky
    asyncio.create_task(choose_lucky())


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
