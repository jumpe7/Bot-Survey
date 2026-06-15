from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database import Session
from models import User

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id

    async with Session() as session:
        user = await session.get(User, user_id)

        if not user:
            session.add(User(telegram_id=user_id))
            await session.commit()

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
