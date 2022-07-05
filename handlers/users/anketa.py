from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states.personaldata import personaldata


@dp.message_handler(Command("anketa"))
async def enter_test(message: types.Message):
    await message.answer("To'liq ismimngizni kiriting")
    await personaldata.fullname.set()



@dp.message_handler(state=personaldata.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(name=fullname)
    await message.answer("Telefon raqamingizni kiriting")
    await personaldata.next()



@dp.message_handler(state=personaldata.phoneNumber)
async def answer_number(message: types.Message, state: FSMContext):

    number = message.text
    await state.update_data(number=number)
    data = await state.get_data()
    name = data.get("name")
    number = data.get("number")



    msg = "Quyidagilar qabul qilindi:\n"
    msg += f"Ismingiz- {name}\n"
    msg += f"Telefon raqamingiz- {number}\n"

    await message.answer(msg)
    await state.finish()
