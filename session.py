from aiogram.fsm.state import StatesGroup, State


class AskState(StatesGroup):
    waiting_message = State()