from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu1
from loader import dp
from keyboards.default.startkeyboard import menustart
from aiogram.types import ReplyKeyboardRemove

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, * {message.from_user.full_name}*!\nBu bot [PMT Prezident Maktabiga Tayyorgarlik](https://t.me/prezident_maktabiga_tayyorlovv)"
                         f" kanalining rasmiy boti.",parse_mode="Markdown", reply_markup=menustart, disable_web_page_preview=True )
    await message.answer(text="Prezident Maktabiga Tayyorgarlik botiga xush kelibsiz.\nO'zingizga kerakli ma'lumotlarni ola olsangiz biz xursand bo'lamiz", reply_markup=menu1)
