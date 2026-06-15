import os
import asyncio

from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from database import create_db
from start import router as start_router
from deep_link import router as deep_link_router
from send_message import router as send_message_router

async def main():
    load_dotenv()
    await create_db()
    BOT_TOKEN = os.getenv("TOKEN")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_router)
    dp.include_router(deep_link_router)
    dp.include_router(send_message_router)

    print('Bot started')
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())