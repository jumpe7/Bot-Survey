from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

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
        'Я бот для анонимных вопросов.'
        '🔗 Твоя персональная ссылка уже готова — поделись ею с друзьями:'
        f'\n{link}\n\n'
        '💬 Через неё тебе смогут писать анонимно.'
    )