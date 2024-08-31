from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

def til():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="O'zbek"),
        KeyboardButton(text="Русский")
    )
    return markup
def asosiymenuuz():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Inspektorning harakatlari/harakatsizligi to‘g‘risidagi shikoyat"),
        KeyboardButton(text="Murojaat holatini tekshirish"),
        KeyboardButton(text="Mening murojaatlarim"),
        KeyboardButton(text="Murojaat jo‘natish"),
        KeyboardButton(text="❌Bekor qilish"),
    )
    return markup
def asosiymenurus():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Жалоба на действия/бездействие инспектора"),
        KeyboardButton(text="Проверить статус заявки"),
        KeyboardButton(text="Мои запрос"),
        KeyboardButton(text="Отправить обращение"),
        KeyboardButton(text="❌Отменить"),
    )
    return markup

def uzbknopka():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="🏛 Bosh Menyu"),
    )
    return markup
def uzbknopka2():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="🏛 Bosh Menyu")
    )
    return markup
def uzbknopka3():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="🏛 Bosh Menyu"),
        KeyboardButton(text="Sizda arizalar mavjudmas")
    )
    return markup
def uzbknopka4():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="F.I.SH"),
        KeyboardButton(text="🏛 Bosh Menyu")
    )
    return markup

def uzbknopka5():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Kontakt yuborish",),
    KeyboardButton(text="🏛 Bosh Menyu")
    )
    return markup

def rusknopka():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="🏛 Главное меню"),
    )
    return markup

def rusknopka2():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="🏛 Главное меню"),
    )
    return markup

def rusknopka3():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="🏛 Главное меню"),
        KeyboardButton(text="У вас нет приложений"),
    )
    return markup

def rusknopka4():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Ф.И.Ш"),
        KeyboardButton(text="🏛 Главное меню"),
    )
    return markup

def rusknopka5():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Отправить контакт",),
        KeyboardButton(text="🏛 Главное меню"),
    )
    return markup