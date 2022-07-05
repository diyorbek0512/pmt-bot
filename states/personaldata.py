from aiogram.dispatcher.filters.state import StatesGroup, State
class personaldata(StatesGroup):
    fullname = State()
    phoneNumber = State()