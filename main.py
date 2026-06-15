import asyncio
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

sessions = {}


class AskState(StatesGroup):
    waiting_message = State()


@router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    bot_username = (await message.bot.get_me()).username
    link = (
        f'https://t.me/'
        f'{bot_username}'
        f'?start={user_id}'
    )

    await message.answer(
        '👋 Привет!\n\n'
        'Я бот для анонимных вопросов.\n'
        '🔗 Твоя персональная ссылка уже готова — поделись ею с друзьями:'
        f'\n{link}\n\n'
        '💬 Через неё тебе смогут писать анонимно.'
    )

    args = message.text.split()
    if len(args) < 1:
        owner_id = int(args[1])
        sessions[user_id] = owner_id

        await message.answer(
            "Напишите анонимное сообщение"
        )
        return



@router.message()
async def handle_message(message: Message):
    sender_id = message.from_user.id

    if sender_id not in sessions:
        await message.answer(
            "Сначала открой свою ссылку через /start"
        )
        return

    receiver_id = sessions[sender_id]

    text = message.text

    await bot.send_message(
        receiver_id,
        "📩 Новый анонимный вопрос:\n\n"
        f"{text}"
    )

    await message.answer(
        "✅ Отправлено анонимно"
    )


    del sessions[sender_id]


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())