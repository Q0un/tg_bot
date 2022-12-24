from main import dp, States
from aiogram import types
from random import randint


@dp.message_handler(commands=['randint'], state=States.no_command)
async def randint_handle(message: types.Message):
    await message.answer("Write two integers which sets range")
    await States.randint.set()


@dp.message_handler(state=States.randint)
async def randint_impl(message: types.Message):
    try:
        x, y = map(int, message.text.split())
    except Exception:
        await message.answer("No! You need to write two integers")
        return
    await message.answer("Your number is " + str(randint(x, y)))
    await States.no_command.set()
