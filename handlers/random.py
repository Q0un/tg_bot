from main import dp, States
from aiogram import types
from random import choice


@dp.message_handler(commands=['random'], state=States.no_command)
async def random_handle(message: types.Message):
    await message.answer("Write set of strings, each one on next line")
    await States.random.set()


@dp.message_handler(state=States.random)
async def random_impl(message: types.Message):
    await message.answer('Your choice is "' + choice(message.text.split('\n')) + '"')
    await States.no_command.set()
