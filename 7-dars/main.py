from aiogram.types import  Message
from aiogram import Bot, Dispatcher, executor
from knopkalar import *

telegramapi = '7351676892:AAFWtnJxxFVTxkrCYnXcOKd3zkhpKD5T1cs'
bot = Bot(telegramapi)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Assalomu alaykum, iltimos tilni tanlang, Здравствуйте, выберите пожалуйста язык", reply_markup=til())

@dp.message_handler(text="O'zbek")
async def getozbek(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🏛 Bosh Menyu', reply_markup=asosiymenuuz())


@dp.message_handler(text="Русский")
async def getrus(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🏛 Главное меню', reply_markup=asosiymenurus())

@dp.message_handler(text="🏛 Главное меню")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="🏛 Главное меню", reply_markup=asosiymenurus())

@dp.message_handler(text="🏛 Bosh Menyu")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="🏛 Bosh Menyu", reply_markup=asosiymenuuz())

@dp.message_handler(text="❌Отменить")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="❌Отменить", reply_markup=til())

@dp.message_handler(text="❌Bekor qilish")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="❌Bekor qilish", reply_markup=til())

@dp.message_handler(text="Inspektorning harakatlari/harakatsizligi to‘g‘risidagi shikoyat")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Iltimos ariza raqamini kiriting", reply_markup=uzbknopka())

@dp.message_handler(text="Murojaat holatini tekshirish")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Iltimos ariza raqamini kiriting", reply_markup=uzbknopka2())

@dp.message_handler(text="Mening murojaatlarim")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Iltimos ariza raqamini tanlang", reply_markup=uzbknopka3())

@dp.message_handler(text="Murojaat jo‘natish")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Iltimos, to‘liq F.I.Sh.ni kiriting.", reply_markup=uzbknopka4())

@dp.message_handler(text="F.I.SH")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Telefon raqamingizni kiriting", reply_markup=uzbknopka5())

@dp.message_handler(text="Жалоба на действия/бездействие инспектора")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Пожалуйста, введите номер заявки", reply_markup=rusknopka())

@dp.message_handler(text="Проверить статус заявки")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Пожалуйста, введите номер заявки", reply_markup=rusknopka2())

@dp.message_handler(text="Мои запрос")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Пожалуйста, введите номер заявки", reply_markup=rusknopka3())

@dp.message_handler(text="Отправить обращение")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Пожалуйста, введите Ф.И.О.", reply_markup=rusknopka4())

@dp.message_handler(text="Ф.И.Ш")
async def getdauzru(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text="Введите свой номер телефона", reply_markup=rusknopka5())


executor.start_polling(dp, skip_updates=True)