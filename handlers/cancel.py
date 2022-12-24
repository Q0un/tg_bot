from main import dp, States
from aiogram import types


@dp.message_handler(commands=['cancel'], state='*')
async def cancel_handle(message: types.Message):
    await message.answer("You can call another method now!")
    await States.no_command.set()
