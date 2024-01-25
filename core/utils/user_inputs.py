from aiogram.fsm.state import StatesGroup, State


class GetUserInput(StatesGroup):
    user_input = State()
