from aiogram.dispatcher.filters.state import StatesGroup, State

class Translate(StatesGroup):
    ism=State()
    familiya=State()
    tel_raqam=State()