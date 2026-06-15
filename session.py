from aiogram.fsm.state import StatesGroup, State

session = {}

class AskState(StatesGroup):
    waiting_message = State()