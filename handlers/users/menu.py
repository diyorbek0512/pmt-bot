from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu2, menu3, menu1, menu5, menu6
from keyboards.default.pythonkeyboard import menupython, menupythona, menupythonb, menupythonc, menupython_gobaack
from loader import dp
from states.statedata import statedata


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("O'zingizga muhim bo'lgan bo'limni tanlashingiz mumkin", reply_markup=menu1)

@dp.message_handler(text="🏫Prezident Maktabi")
async def ksa(message: Message):
    await message.answer("Quyidagilarni tanlang", reply_markup=menu2)

@dp.message_handler(text="❇Prezident Maktabi Hayoti❇")
async def sas(message: Message):
    await message.answer_video("https://t.me/fornothing0/8", caption="Prezident Maktabi hayoti haqida to'liq video bilan tanishib chiqing! \n\n@pmt_test")
@dp.message_handler(text="❔❓Namunaviy savollar")
async def dasdasd(message: Message):
    await message.answer(text="Quyidagi fanlardan birini tanlang:", reply_markup=menu3)
@dp.message_handler(text="📐Matematika")
async def show_c4gdoki(message: Message):
    await message.answer_photo("https://t.me/pmt_test/88", caption="@pmt_test")
    await message.answer_photo("https://t.me/pmt_test/89", caption="@pmt_test")
    await message.answer_photo("https://t.me/pmt_test/90", caption="@pmt_test")
    await message.answer_photo("https://t.me/pmt_test/91", caption="@pmt_test")
    await message.answer_photo("https://t.me/pmt_test/92", caption="@pmt_test")
    await message.answer_photo("https://t.me/pmt_test/93", caption="@pmt_test")
    await message.answer_photo("https://t.me/pmt_test/94", caption="@pmt_test")
    await message.answer_photo("https://t.me/pmt_test/95", caption="@pmt_test")
    await message.answer_photo("https://t.me/pmt_test/96", caption="@pmt_test")
    await message.answer(text="Javoblaringizni yuboring")
    await statedata.salom.set()

@dp.message_handler(state=statedata.salom)
async def echmo(message: types.Message, state: FSMContext):
    y = "cdeacdcbbcacbdbbbbdd"
    cnt = 0
    @dp.message_handler(text="Go Back.")
    async def show_phop(message: Message):
        await state.finish()
        await message.answer(text="Quyidagilarni tanlang", reply_markup=menu1)
    if len(message.text) == 20:
        for i in range(len(message.text)):
            if message.text[i] != y[i]:
                cnt += 1
        ll = (20 - cnt) * 5
        await message.answer(text=f"20ta savoldan {20-cnt}ta topib, {ll}% natijani qo'lga kiritdingiz, ofarin!")
        await state.finish()

    else:
        await message.answer(text="Siz kiritgan javoblar soni 20taga teng emas, tekshirib qaytadan jo'nating!", reply_markup=menupython_gobaack)
        await state.finish()
        @dp.message_handler(text="Go Back.")
        async def show_phop(message: Message):
            await state.finish()
            await message.answer(text="Quyidagilarni tanlang", reply_markup=menu1)


@dp.message_handler(text="Go Back.")
async def show_phop(message: Message):
    await message.answer(text="Quyidagilarni tanlang", reply_markup=menu1)


@dp.message_handler(text="📗 Tanqidiy Fikrlash")
async def show_msg(message: Message):
    await message.answer_document("https://t.me/fornothing0/9",caption="@pmt_test")

@dp.message_handler(text="📖 Ingliz tili")
async def show_msg(message: Message):
    await message.answer_document("https://t.me/fornothing0/10", caption="@pmt_test")

#
# @dp.message_handler(text="📖Tanqidiy Fikrlash")
# async def show_msg(message: Message):
#     await message.answer(text="👇👇👇Tanlang", reply_markup=menupython)
#
#
# @dp.message_handler(text="📜Ma'lumot")
# async def show_b(message: Message):
#     await message.answer(
#         text="📁Prezident Maktabi Imtixonining 2-bosqichidan o'tish uchun alohida chuqur tayyorgarlik bo'yicha pdf formatda *Tanqidiy Fikrlash* to'plamini xarid qilishingiz mumkin✅\n📎U tòplam 500sahifali bòlib ichida 400xil savollarning har birining ishlanish usullari bilan bor✅",
#         parse_mode="Markdown")
#
#
# @dp.message_handler(text="📋Namuna")
# async def show_ha(message: Message):
#     await message.answer_photo('https://t.me/qmkdetb/31', caption="Tanqidiy Fikrlash namuna")
#
#
# @dp.message_handler(text="🛒Xarid Qilish")
# async def show_ha(message: Message):
#     await message.answer(text="📥Xarid Qilishingiz uchun telegram orqali \n @school_admin0 ga yozing✅")
#
#
# @dp.message_handler(text="📙Muammoli Masalalar")
# async def show_msg(message: Message):
#     await message.answer(text="👇👇👇Tanlang", reply_markup=menupythona)
#
#
# @dp.message_handler(text="📜Ma'lumot.")
# async def show_b(message: Message):
#     await message.answer(
#         text="📁Prezident Maktabi Imtixonining 2-bosqichidan o'tish uchun alohida chuqur tayyorgarlik bo'yicha pdf formatda *Muammoli Masalalar* to'plamini xarid qilishingiz mumkin✅\n📎U tòplam 500sahifali bòlib ichida 400xil savollarning har birining ishlanish usullari bilan bor✅",
#         parse_mode="Markdown")
#
#
# @dp.message_handler(text="📋Namuna.")
# async def show_ha(message: Message):
#     await message.answer_photo("https://t.me/qmkdetb/32", caption='Muammoli Masalalar')
#
#
# @dp.message_handler(text="🛒Xarid Qilish")
# async def show_ha(message: Message):
#     await message.answer(text="📥Xarid Qilishingiz uchun telegram orqali \n @school_admin0 ga yozing✅")
#
#
# @dp.message_handler(text="🧮Matematika")
# async def show_haha(message: Message):
#     await message.answer(text="👇👇👇Tanlang", reply_markup=menupythonb)
#
#
# @dp.message_handler(text="📜Ma'lumot .")
# async def show_haim(message: Message):
#     await message.answer(
#         text="📁Prezident Maktabi Imtixonining 1-bosqichidan o'tish uchun alohida chuqur tayyorgarlik bo'yicha pdf formatda *Matematika* nomli to'plam orqali o'z ustingizda tayyorgarlik ko'rishingiz mumkin✅",
#         parse_mode="Markdown")
#
#
#
# @dp.message_handler(text="📖Ingliz tili")
# async def show_aka(message: Message):
#     await message.answer(text="👇👇👇Tanlang", reply_markup=menupythonc)
#
#
# @dp.message_handler(text="📜 Ma'lumot")
# async def show_how(message: Message):
#     await message.answer(
#         text="📁Prezident Maktabi Imtixonining 2-bosqichidan o'tish uchun alohida chuqur tayyorgarlik uchun <b><u>Ingliz Tili</u></b> dan <em>Reading</em>, <em>Grammar</em> yo'nalishlari bo'yicha tuzilgan kitobdan o'z ustingizda ishlashingiz va darajangizni ko'tarib olishingiz mumkin✅",
#         parse_mode="Html")
#
#
# @dp.message_handler(text="🔰Namuna")
# async def show_alkali(message: Message):
#     await message.answer_photo("https://t.me/qmkdetb/33", caption="Ingliz tili \nTo'plamdan namuna")
#
# @dp.message_handler(text="Go back.")
# async def show_kali(message: Message):
#     await message.answer("O'zingizga muhim bo'lgan bo'limni tanlashingiz mumkin", reply_markup=menu1)

# @dp.message_handler(text="🔍MAXSUS TO'PLAM")
# async def sjwww(message: Message):
#     await message.answer("O'zingizga kerakli to'plamni tanlang va ma'lumotlarga ega bo'ling!", reply_markup=menu4)
#
#
# @dp.message_handler(text="Go Back")
# async def show_kali(message: Message):
#     await message.answer("Kerakli bo'limni tanlang", reply_markup=menu4)
#

@dp.message_handler(text="🗂Tayyorgarlik uchun darslar")
async def shw(message: Message):
    await message.answer(text="Kerakli bo'limni tanlang", reply_markup=menu5)
@dp.message_handler(text="📈 Tanqidiy fikrlash")
async def ss(message: Message):
    await message.answer_video("https://t.me/fornothing0/11", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/12", caption="@pmt_test")
    await message.answer(text="https://www.youtube.com/watch?v=067kc_LBwFo")
@dp.message_handler(text="📖 Matematika")
async def ss(message: Message):
    await message.answer_video("https://t.me/fornothing0/13", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/14", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/15", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/16", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/17", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/18", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/19", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/20", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/21", caption="@pmt_test")
    await message.answer_video("https://t.me/fornothing0/12", caption="@pmt_test")


@dp.message_handler(text="📣Telegram Kanalga ulanish")
async def dfasssscp(message: Message):
    await message.answer(text="[Kanalga ulanish](https://t.me/pmt_test)", parse_mode="Markdown")



@dp.message_handler(text="▶YouTube kanalga ulanish")
async def dfasssscp(message: Message):
    await message.answer(text="https://www.youtube.com/c/PREZIDENTmaktabigabepultayyorlovkursi")

@dp.message_handler(text="🏫Ixtisoslashtirilgan Maktablar")
async def asds(message: Message):
    await message.answer("Kerakli fanni tanlang", reply_markup=menu6)


@dp.message_handler(text="Ingliz Tili")
async def asdasxs(message: Message):
    await message.answer_document("https://t.me/fornothing0/24?single", caption="5-sinf")
    await message.answer_document("https://t.me/fornothing0/26?single", caption="6-sinf")
    await message.answer_document("https://t.me/fornothing0/29?single", caption="7-sinf")
    await message.answer_document("https://t.me/fornothing0/33?single", caption="8-sinf")
    await message.answer_document("https://t.me/fornothing0/36?single", caption="9-sinf")
    await message.answer_document("https://t.me/fornothing0/42?single", caption="10-sinf")
    await message.answer_document("https://t.me/fornothing0/47?single", caption="11-sinf")

@dp.message_handler(text="Matematika")
async def asxds(message: Message):
    await message.answer_document("https://t.me/fornothing0/23?single", caption="5-sinf")
    await message.answer_document("https://t.me/fornothing0/25?single", caption="6-sinf")
    await message.answer_document("https://t.me/fornothing0/28?single", caption="7-sinf")
    await message.answer_document("https://t.me/fornothing0/31?single", caption="8-sinf")
    await message.answer_document("https://t.me/fornothing0/39?single", caption="9-sinf")
    await message.answer_document("https://t.me/fornothing0/45?single", caption="10-sinf")
    await message.answer_document("https://t.me/fornothing0/49?single", caption="11-sinf")

@dp.message_handler(text="Fizika")
async def asdas(message: Message):
    await message.answer_document("https://t.me/fornothing0/27?single", caption="7-sinf")
    await message.answer_document("https://t.me/fornothing0/32?single", caption="8-sinf")
    await message.answer_document("https://t.me/fornothing0/38?single", caption="9-sinf")
    await message.answer_document("https://t.me/fornothing0/43?single", caption="10-sinf")
    await message.answer_document("https://t.me/fornothing0/48?single", caption="11-sinf")


@dp.message_handler(text="Biologiya")
async def asds(message: Message):
    await message.answer_document("https://t.me/fornothing0/30?single", caption="7-sinf")
    await message.answer_document("https://t.me/fornothing0/34?single", caption="8-sinf")
    await message.answer_document("https://t.me/fornothing0/40?single", caption="9-sinf")
    await message.answer_document("https://t.me/fornothing0/44?single", caption="10-sinf")
    await message.answer_document("https://t.me/fornothing0/50?single", caption="11-sinf")


@dp.message_handler(text="Kimyo")
async def assds(message: Message):
    await message.answer_document("https://t.me/fornothing0/35?single", caption="8-sinf")
    await message.answer_document("https://t.me/fornothing0/37?single", caption="9-sinf")
    await message.answer_document("https://t.me/fornothing0/41?single", caption="10-sinf")
    await message.answer_document("https://t.me/fornothing0/46?single", caption="11-sinf")

@dp.message_handler(text="Matematikadan video darslar")
async def assds(message: Message):
    await message.answer("\nHurmatli 6-sinf o'quvchilari,\n\n✅Ixtisoslashtirilgan maktablarga imtihondan yaxshi natijani qo'lga kiritishni niyat qilgan bo'lsangiz, yangi ishlab chiqilgan video aynan sizlar uchun!\n🗞Matematikadan namunaviy savollarning 6-sinf testlari tahlilini ko'rib chiqmoqchi bo'lsangiz\n[linkni ustiga bosing](https://www.youtube.com/watch?v=q_mWtGNdiSY) \n✏Tahlilni YOU TUBE kanalimizda tomosha qiling\n\n\n⬇Bizni ijtimoiy tarmoqlarda kuzatib boring:\n[Telegram](https://t.me/prezident_maktabiga_tayyorlovv) | [YouTube](https://www.youtube.com/channel/UCc1V7a6zG7UfjNwR8jsEpuA/)", parse_mode="Markdown")
    await message.answer("\nHurmatli 7-sinf o'quvchilari,\n\n✅Ixtisoslashtirilgan maktablarga imtihondan yaxshi natijani qo'lga kiritishni niyat qilgan bo'lsangiz, yangi ishlab chiqilgan video aynan sizlar uchun!\n🗞Matematikadan namunaviy savollarning 7-sinf testlari tahlilini ko'rib chiqmoqchi bo'lsangiz  [linkni ustiga bosing](https://youtu.be/Kyfdp825zVQ) \n✏️Tahlilni YOU TUBE kanalimizda tomosha qiling\n\n\n⬇Bizni ijtimoiy tarmoqlarda kuzatib boring:\n[Telegram](https://t.me/prezident_maktabiga_tayyorlovv) | [YouTube](https://www.youtube.com/channel/UCc1V7a6zG7UfjNwR8jsEpuA/)", parse_mode="Markdown")

@dp.message_handler(text="Go BacK")
async def addaaaq(message: Message):
    await message.answer("O'zingizg"
                         "a muhim bo'lgan bo'limni tanlashingiz mumkin!", reply_markup=menu1)

@dp.message_handler(text="💻Reklama xizmati")
async def adsd1qm(message: Message):
    await message.answer("💻Reklama xizmatiga xush kelibsiz!\nBu bot orqali o'zingizning ilmiy reklamalaringizni tarqatishingiz mumkin.\n✅Buning uchun @school_admin0 bilan aloqaga chiqing")