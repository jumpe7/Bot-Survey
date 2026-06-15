from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from database import Session
from models import AnonymousMessage

from session import AskState

router = Router()

@router.message(AskState.waiting_message)
async def send_anonymous_message(message:Message, state: FSMContext):
    data = await state.get_data()
    receiver_id = data['receiver_id']
    sender_id = data['sender_id']
    text = message.text

    async with Session() as session:
        session.add(AnonymousMessage(receiver_id=receiver_id, sender_id=sender_id, text=text))

        await session.commit()

    await message.bot.send_message(receiver_id,
                                   'Вам пришло новое'
                                        'анонимное сообщение:\n\n'
                                        f'{text}')
    await message.answer("Сообщение отправлено.")

    await state.clear()