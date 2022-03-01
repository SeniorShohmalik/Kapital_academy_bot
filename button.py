from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kurslar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="IT bo`yicha kurslar💻"),KeyboardButton(text="Fanlar bo`yicha kurslar👩‍🎓")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
fanlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Tabiiy fanlar🌎"),KeyboardButton(text="Ijtimoiy fanlar📖")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
ijtimoiy_fanlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ona tili va adabiyot📗"),KeyboardButton(text="Ingliz tili📒")],
        [KeyboardButton(text="Rus tili📓"),KeyboardButton(text="Tarix📚")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
aniq_fanlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Matematika👨🏻‍🏫"),KeyboardButton(text="Fizika👩🏼‍🏫")],
        [KeyboardButton(text="Kimyo👨‍🔬"),KeyboardButton(text="Biologiya👩‍🔬")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
IT = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="3D MAX 🏦"),KeyboardButton(text="Frontend🤩")],
        [KeyboardButton(text="Komputer savodxonligi🖥")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
join = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kursda qatnashmoqchiman👩🏼‍🏫")],
        [KeyboardButton(text="Menuga qaytish📔")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
