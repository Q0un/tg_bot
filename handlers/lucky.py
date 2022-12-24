from main import dp, States
from aiogram import types
import asyncio
from random import choice


people = []


@dp.message_handler(commands=['signup'], state=States.no_command)
async def signup_handle(message: types.Message):
    for p in people:
        if message.from_id == p.from_id:
            await message.answer("You were already registered!")
            return
    people.append(message)
    await message.answer("You were registered to the contest!")


@dp.message_handler(commands=['forgetme'], state=States.no_command)
async def signup_handle(message: types.Message):
    for p in people:
        if message.from_id == p.from_id:
            people.remove(p)
            await message.answer("You will no longer participate in contest!")
            return
    await message.answer("You were not registered to the contest!")


async def choose_lucky():
    while True:
        if len(people) > 0:
            await choice(people).answer("You are lucky person today! Congratulations!!")
        await asyncio.sleep(86400)
