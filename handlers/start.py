from main import dp, States
from aiogram import types


async def send_help(message: types.Message):
    await message.answer("Hi!\n"
                         "There are 5 methods in this bot:\n"
                         "/help - Get this message\n"
                         "/randint - Generates random integer in range\n"
                         "/random - Picks random string from set\n"
                         "/calculate - Calculates string\n"
                         "/signup - Sign up to the everyday contest of being lucky man\n"
                         "/forgetme - You will no longer participate in everyday contest\n"
                         "And you can always use\n"
                         "/cancel - To exit from method execution\n")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await send_help(message)
    await States.no_command.set()


@dp.message_handler(commands=['help'], state='*')
async def help_handler(message: types.Message):
    await send_help(message)
