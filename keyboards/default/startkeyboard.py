from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menustart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True)
        ]
    ],resize_keyboard=True
)