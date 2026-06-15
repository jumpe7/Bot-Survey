import asyncio

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message()
async def echo_handler(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Хорошая попытка')

async def main():
    load_dotenv()
    tg_tok = getenv("TOKEN")
    bot = Bot(token=tg_tok)
    print('Бот запущен!')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())