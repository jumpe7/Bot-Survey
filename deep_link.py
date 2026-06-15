from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from aiogram.types import Message

from session import AskState

router = Router()

@router.message(CommandStart, deep_link=True)
async def anonymous_entry(message: Message, state: FSMContext):
    args = message.text.split()
    if len(args) < 2:
        return
    receiver_id = int(args[1])

    await state.update_data(receiver_id=receiver_id)

    await message.answer('Напишите анонимное сообщение')
