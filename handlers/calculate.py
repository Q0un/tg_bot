from main import dp, States
from aiogram import types


allowed = "0123456789+-/* "


@dp.message_handler(commands=['calculate'], state=States.no_command)
async def calc_handle(message: types.Message):
    await message.answer("Write line which you want to calculate")
    await States.calc.set()


@dp.message_handler(state=States.calc)
async def calc_impl(message: types.Message):
    for c in message.text:
        if c not in allowed:
            await message.answer("Bad string!")
            return
    await message.answer("Your answer is " + str(eval(message.text)))
    await States.no_command.set()
