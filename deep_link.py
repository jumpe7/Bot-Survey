from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext

from aiogram.types import Message

from session import AskState

router = Router()

@router.message(CommandStart)
async def anonymous_entry(message: Message, state: FSMContext, command: CommandObject):
    if not command.args:
        return

    try:
        receiver_id = int(command.args)
    except ValueError:
        await message.answer('Некорректная ссылка')
        return

    await state.update_data(receiver_id=receiver_id)

    await state.set_state(AskState.waiting_message)


    await message.answer('Напишите анонимное сообщение')
