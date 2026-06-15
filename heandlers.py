from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from session import session

router = Router()

@router.message()
async def handle_message(message: Message):
    sender_id = message.from_user.id

    if sender_id not in session:
        await message.answer("Сначала открой свою ссылку через /start")
        return
    receiver_id = session[sender_id]
    text = message.text
