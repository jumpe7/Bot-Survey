import asyncio

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from start import router as start_router


async def main():
    dp = Dispatcher()
    load_dotenv()
    BOT_TOKEN = getenv("TOKEN")
    bot = Bot(token=BOT_TOKEN)
    print('Бот запущен!')
    dp.include_router(
        start_router
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())