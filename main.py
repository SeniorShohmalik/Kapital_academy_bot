import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import state
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext 
from button import aniq_fanlar,fanlar,kurslar,ijtimoiy_fanlar,IT,join
from state import Translate
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user}😊\nBizning botimizga xush kelibsiz😄\nTuzuvchi @deSeniorCoder😄", reply_markup=kurslar)
# IT bo'yicha kurslar
@dp.message_handler(Text(equals=['IT bo`yicha kurslar💻']))
async def my_course(message,state:FSMContext):
    await message.answer('Bizning IT bo`yicha kurslarimiz!?',reply_markup=IT)
@dp.message_handler(Text(equals=['3D MAX 🏦']))
async def my_course(message,state:FSMContext):
    await message.answer('Hozircha bu yer bo`sh',reply_markup=join)
@dp.message_handler(Text(equals=['Frontend🤩']))
async def my_course(message,state:FSMContext):
    await message.answer('Hozircha bu yer bo`sh',reply_markup=join)
@dp.message_handler(Text(equals=['Komputer savodxonligi🖥']))
async def my_course(message,state:FSMContext):
    await message.answer('Hozircha bu yer bo`sh',reply_markup=join)
# fanlar bo'yicha kurslar
@dp.message_handler(Text(equals=['Fanlar bo`yicha kurslar👩‍🎓']))
async def my_course(message,state:FSMContext):
    await message.answer('Bizda mavjud fanlar!?',reply_markup=fanlar)
@dp.message_handler(Text(equals=['Tabiiy fanlar🌎']))
async def my_course(message,state:FSMContext):
    await message.answer('Aniq fanlar',reply_markup=aniq_fanlar)
@dp.message_handler(Text(equals=['Ijtimoiy fanlar📖']))
async def my_course(message,state:FSMContext):
    await message.answer('Ijtimoiy fanlar',reply_markup=ijtimoiy_fanlar)
@dp.message_handler(Text(equals=['Matematika👨🏻‍🏫']))
async def my_course(message,state:FSMContext):
    await message.answer('Bu yer hozircha bo`sh',reply_markup=join) 
@dp.message_handler(Text(equals=['Fizika👩🏼‍🏫']))
async def my_course(message,state:FSMContext):
    await message.answer('Bu yer hozircha bo`sh',reply_markup=join)
@dp.message_handler(Text(equals=['Kimyo👨‍🔬']))
async def my_course(message,state:FSMContext):
    await message.answer('Bu yer hozircha bo`sh',reply_markup=join)
@dp.message_handler(Text(equals=['Biologiya👩‍🔬']))
async def my_course(message,state:FSMContext):
    await message.answer('Bu yer hozircha bo`sh',reply_markup=join)
@dp.message_handler(Text(equals=['Ona tili va adabiyot📗']))
async def my_course(message,state:FSMContext):
    await message.answer('Bu yer hozircha bo`sh',reply_markup=join)
@dp.message_handler(Text(equals=['Ingliz tili📒']))
async def my_course(message,state:FSMContext):
    await message.answer('Kurs davomiyligi:Nomalum\nNarxi:Nomalum',reply_markup=join) 
@dp.message_handler(Text(equals=['Rus tili📓']))
async def my_course(message,state:FSMContext):
    await message.answer('Bu yer hozircha bo`sh',reply_markup=join)
@dp.message_handler(Text(equals=['Tarix📚']))
async def my_course(message,state:FSMContext):
    await message.answer('Bu yer hozircha bo`sh',reply_markup=join)
# ro'yxattan o'tish
@dp.message_handler(Text(equals=['Kursda qatnashmoqchiman👩🏼‍🏫']))
async def my_course(message,state:FSMContext):
    await message.answer('Iltimos ismingizni kiriting👨‍🎓🧑‍🎓')
    await Translate.ism.set()
@dp.message_handler(state=Translate.ism)
async def my_course(message,state:FSMContext):
    await message.answer('Iltimos familiyangzni kiriting👨‍🦳')
    ism=message.text
    await state.update_data({'ism':ism})
    await Translate.familiya.set()
@dp.message_handler(state=Translate.familiya)
async def my_course(message,state:FSMContext):
    await message.answer('Iltimos telefon raqamingizni kiriting☎️')
    familiya=message.text
    await state.update_data({'familiya':familiya})
    await Translate.tel_raqam.set()
@dp.message_handler(state=Translate.tel_raqam)
async def my_course(message,state:FSMContext):
    if message.text[0:4]=='+998' and len(message.text)==13:
        await message.answer('Siz ro`yxattan muvaffaqiyatli o`tdingiz✅\nTez orada sizga adminlar qo`ngiroq qiladi☎️')
        tel=message.text
        data = await state.get_data()
        ism=data.get('ism')
        familiya=data.get('familiya')
        await bot.send_message(chat_id=866872982,text=f'Bazaga yangi o`quvchi qo`shildi👩‍🎓👨‍🎓\nIsmi:{ism}\nFamiliyasi:{familiya}\nTelefon raqami☎️:{tel}')
        await state.finish()
        await message.answer('Bosh menu',reply_markup=kurslar)
    else:
        await message.answer(f'Raqamingizni to`gri kiriting:M-n(+998974748110)')




@dp.message_handler(Text(equals=['Menuga qaytish📔']))
async def my_course(message,state:FSMContext):
    await message.answer('Siz bosh bo\'limdasiz',reply_markup=kurslar)
    






if  __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    # data = await state.get_data()
    # r1 = data.get("borish")
    # r2=data.get("manzil")
    # await message.answer(f'{r1}','{r2}')
    # borish = message.text
    # await state.update_data(
    #     {"borish": borish},
    # )