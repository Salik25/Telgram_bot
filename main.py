import requests
import telebot
from telebot import types

TOKEN = '933830649:AAGwMokxU0gme7sQt44ezbzdTVrcBm4LclI'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help'])
def help_me(message):
    bot.send_message(message.chat.id, "Я научу тебя мной пользоваться.")
    bot.send_message(message.chat.id, "Выбери билет в меню и тебе пришлется фото-ответ. Твоя задача только не заметно списать.")
    bot.send_message(message.chat.id, "1) ЭМИ - Явление электромагнитной индукции (ЭМИ). Правило Ленца. Способы изменения магнитного потока. Практическое использование ЭМИ. Токи Фуко.\n"
                                      "2) Магнитный поток самоиндукции - Магнитный поток самоиндукции. Индуктивность. Индуктивность бесконечного соленоида.\n"
                                      "3) ЭДС самоиндукции - ЭДС самоиндукции. Энергия магнитного поля.\n"
                                      "4) Токи при замыкании и размыкании цепи - Токи при замыкании и размыкании цепи\n"
                                      "5) Вихревое электрическое поле - Вихревое электрическое поле. Первое уравнение Максвелла для электромагнитного поля\n"
                                      "6) Ток смещения - Ток смещения. Второе уравнение Максвелла для электромагнитного поля.\n"
                                      "7) Система уравнений Максвелла - Полная система уравнений Максвелла для электромагнитного поля (в интегральной форме).\n"
                                      "8) Колебания и их характеристики - Колебания и их характеристики. Механические гармонические колебания. Скорость и ускорение при гармонических колебаниях.\n"
                                      "9) Гармонический осциллятор - Гармонический осциллятор. Пружинный и математический маятники.\n"
                                      "10) Физический маятник - Физический маятник. Приведенная длина физического маятника.\n"
                                      "11) Энергия гармонических колебаний - Энергия гармонических колебаний. Сложение гармонических колебаний одного направления. Биения.\n"
                                      "12) Сложение взаимно перпендикулярных колебаний - Сложение взаимно перпендикулярных колебаний (получить выражение для результирующего колебания при одинаковых частотах). Фигуры Лиссажу.\n"
                                      "13) Затухающие колебания и их характеристики - Затухающие колебания и их характеристики.\n"
                                      "14) Вынужденные колебания - Вынужденные колебания. Явление резонанса.\n"
                                      "15) Колебательный контур - Колебательный контур. Электромагнитные колебания.\n"
                                      "16) Упругие волны - Упругие волны. Продольные и поперечные волны. Характеристики волны.\n"
                                      "17) Уравнение плоской гармонической волны - Уравнение плоской гармонической волны. Волновое уравнение.\n"
                                      "18) Стоячие волны - Стоячие волны.\n"
                                      "19) Электромагнитные волны как следствие уравнений Максвелла - Электромагнитные волны как следствие уравнений Максвелла. Свойства ЭМВ.\n"
                                      "20) Шкала электромагнитных излучений - Шкала электромагнитных излучений. Энергия и импульс ЭМВ. Вектор УмоваПойтинга.\n"
                                      "21) Интерференция волн (света) - Интерференция волн (света). Условия максимумов и минимумов. Когерентные волны.\n"
                                      "22) Пространственная и временная когерентность - Пространственная и временная когерентность.\n"
                                      "23) Наблюдение интерференции света методом деления фронта волны - Наблюдение интерференции света методом деления фронта волны. Опыт Юнга. Ширина интерференционной полосы.\n"
                                      "24) Наблюдение интерференции света методом деления амплитуды волны - Наблюдение интерференции света методом деления амплитуды волны. Интерференция в тонких пленках: полосы равного наклона и полосы равной толщины.\n"
                                      "25) Кольца Ньютона - Кольца Ньютона.\n"
                                      "26) Практическое использование явления интерференции - Практическое использование явления интерференции.\n"
                                      "27) Дифракция света - Дифракция света. Принцип Гюйгенса и Гюйгенса-Френеля.\n"
                                      "28) Зоны Френеля - Зоны Френеля. Результирующая амплитуда в зависимости от числа открытых зон Френеля.\n"
                                      "29) Дифракция Френеля на круглом отверстии и на диске - Дифракция Френеля на круглом отверстии и на диске.\n"
                                      "30) Дифракция Фраунгофера на щели - Дифракция Фраунгофера на щели.\n"
                                      "31) Дифракция Фраунгофера на дифракционной решетке - Дифракция Фраунгофера на дифракционной решетке.\n")


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('ЭМИ')  # Явление электромагнитной индукции
    item2 = types.KeyboardButton('Магнитный поток самоиндукции')
    item3 = types.KeyboardButton('ЭДС самоиндукции')
    item4 = types.KeyboardButton('Токи при замыкании и размыкании цепи')
    item5 = types.KeyboardButton('Вихревое электрическое поле')
    item6 = types.KeyboardButton('Ток смещения')
    item7 = types.KeyboardButton('Система уравнений Максвелла')
    item8 = types.KeyboardButton('Колебания и их характеристики')
    item9 = types.KeyboardButton('Гармонический осциллятор')
    item10 = types.KeyboardButton('Физический маятник')
    item11 = types.KeyboardButton('Энергия гармонических колебаний')
    item12 = types.KeyboardButton('Сложение взаимно перпендикулярных колебаний')
    item13 = types.KeyboardButton('Затухающие колебания и их характеристики')
    item14 = types.KeyboardButton('Вынужденные колебания')
    item15 = types.KeyboardButton('Колебательный контур')
    item16 = types.KeyboardButton('Упругие волны')
    item17 = types.KeyboardButton('Уравнение плоской гармонической волны')
    item18 = types.KeyboardButton('Стоячие волны')
    item19 = types.KeyboardButton('Электромагнитные волны как следствие уравнений Максвелла')
    item20 = types.KeyboardButton('Шкала электромагнитных излучений')
    item21 = types.KeyboardButton('Интерференция волн (света)')
    item22 = types.KeyboardButton('Пространственная и временная когерентность')
    item23 = types.KeyboardButton('Наблюдение интерференции света методом деления фронта волны')
    item24 = types.KeyboardButton('Наблюдение интерференции света методом деления амплитуды волны')
    item25 = types.KeyboardButton('Кольца Ньютона')
    item26 = types.KeyboardButton('Практическое использование явления интерференции')
    item27 = types.KeyboardButton('Дифракция света')
    item28 = types.KeyboardButton('Зоны Френеля')
    item29 = types.KeyboardButton('Дифракция Френеля на круглом отверстии и на диске')
    item30 = types.KeyboardButton('Дифракция Фраунгофера на щели')
    item31 = types.KeyboardButton('Дифракция Фраунгофера на дифракционной решетке')

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14,
               item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27,
               item28, item29, item30, item31)

    bot.send_message(message.chat.id, "Выбери билет: ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def first(message):
    if message.text == 'ЭМИ':
        bot.send_message(message.chat.id,
                         "Явление электромагнитной индукции (ЭМИ). Правило Ленца. Способы изменения магнитного потока. Практическое использование ЭМИ. Токи Фуко.")
        photo = open('images/1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Магнитный поток самоиндукции':
        bot.send_message(message.chat.id,
                         "Магнитный поток самоиндукции. Индуктивность. Индуктивность бесконечного соленоида.")
        photo = open('images/2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'ЭДС самоиндукции':
        bot.send_message(message.chat.id, "ЭДС самоиндукции. Энергия магнитного поля.")
        photo = open('images/3.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Токи при замыкании и размыкании цепи':
        bot.send_message(message.chat.id, "Токи при замыкании и размыкании цепи")
        photo = open('images/4.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Вихревое электрическое поле':
        bot.send_message(message.chat.id,
                         "Вихревое электрическое поле. Первое уравнение Максвелла для электромагнитного поля")
        photo = open('images/5.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Ток смещения':
        bot.send_message(message.chat.id, "Ток смещения. Второе уравнение Максвелла для электромагнитного поля.")
        photo = open('images/6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Система уравнений Максвелла':
        bot.send_message(message.chat.id,
                         "Полная система уравнений Максвелла для электромагнитного поля (в интегральной форме).")
        photo = open('images/7.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Колебания и их характеристики':
        bot.send_message(message.chat.id,
                         "Колебания и их характеристики. Механические гармонические колебания. Скорость и ускорение при гармонических колебаниях.")
        photo = open('images/8.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Гармонический осциллятор':
        bot.send_message(message.chat.id, "Гармонический осциллятор. Пружинный и математический маятники.")
        photo = open('images/9.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Физический маятник':
        bot.send_message(message.chat.id, "Физический маятник. Приведенная длина физического маятника.")
        photo = open('images/10.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Энергия гармонических колебаний':
        bot.send_message(message.chat.id,
                         "Энергия гармонических колебаний. Сложение гармонических колебаний одного направления. Биения.")
        photo = open('images/11.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Сложение взаимно перпендикулярных колебаний':
        bot.send_message(message.chat.id,
                         "Сложение взаимно перпендикулярных колебаний (получить выражение для результирующего колебания при одинаковых частотах). Фигуры Лиссажу.")
        photo = open('images/12.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Затухающие колебания и их характеристики':
        bot.send_message(message.chat.id, "Затухающие колебания и их характеристики.")
        photo = open('images/13.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Вынужденные колебания':
        bot.send_message(message.chat.id, "Вынужденные колебания. Явление резонанса.")
        photo = open('images/14.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Колебательный контур':
        bot.send_message(message.chat.id, "Колебательный контур. Электромагнитные колебания.")
        photo = open('images/15.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Упругие волны':
        bot.send_message(message.chat.id, "Упругие волны. Продольные и поперечные волны. Характеристики волны.")
        photo = open('images/16.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Уравнение плоской гармонической волны':
        bot.send_message(message.chat.id, "Уравнение плоской гармонической волны. Волновое уравнение.")
        photo = open('images/17.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Стоячие волны':
        bot.send_message(message.chat.id, "Стоячие волны.")
        photo = open('images/18.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Электромагнитные волны как следствие уравнений Максвелла':
        bot.send_message(message.chat.id, "Электромагнитные волны как следствие уравнений Максвелла. Свойства ЭМВ.")
        photo = open('images/19.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Шкала электромагнитных излучений':
        bot.send_message(message.chat.id,
                         "Шкала электромагнитных излучений. Энергия и импульс ЭМВ. Вектор УмоваПойтинга.")
        photo = open('images/20.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Интерференция волн (света)':
        bot.send_message(message.chat.id,
                         "Интерференция волн (света). Условия максимумов и минимумов. Когерентные волны.")
        photo = open('images/21.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)


    elif message.text == 'Пространственная и временная когерентность':
        bot.send_message(message.chat.id, "Пространственная и временная когерентность.")
        photo = open('images/22.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Наблюдение интерференции света методом деления фронта волны':
        bot.send_message(message.chat.id, "Наблюдение интерференции света методом деления фронта волны. Опыт Юнга. Ширина интерференционной полосы.")
        photo = open('images/23.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Наблюдение интерференции света методом деления амплитуды волны':
        bot.send_message(message.chat.id, "Наблюдение интерференции света методом деления амплитуды волны. Интерференция в тонких пленках: полосы равного наклона и полосы равной толщины.")
        photo = open('images/24.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Кольца Ньютона':
        bot.send_message(message.chat.id, "Кольца Ньютона.")
        photo = open('images/25.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Практическое использование явления интерференции':
        bot.send_message(message.chat.id, "Практическое использование явления интерференции.")
        photo = open('images/26.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Дифракция света':
        bot.send_message(message.chat.id, "Дифракция света. Принцип Гюйгенса и Гюйгенса-Френеля.")
        photo = open('images/27.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Зоны Френеля':
        bot.send_message(message.chat.id, "Зоны Френеля. Результирующая амплитуда в зависимости от числа открытых зон Френеля.")
        photo = open('images/28.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Дифракция Френеля на круглом отверстии и на диске':
        bot.send_message(message.chat.id, "Дифракция Френеля на круглом отверстии и на диске.")
        photo = open('images/29.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Дифракция Фраунгофера на щели':
        bot.send_message(message.chat.id, "Дифракция Фраунгофера на щели.")
        photo = open('images/30.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Дифракция Фраунгофера на дифракционной решетке':
        bot.send_message(message.chat.id, "Дифракция Фраунгофера на дифракционной решетке.")
        photo = open('images/31.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

while True:
    bot.polling(none_stop=True)
