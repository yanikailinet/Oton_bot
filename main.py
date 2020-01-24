import telebot
from telebot import types

token = "703356954:AAHnGvHB0KE-mpkkH_pWwOBHItxu8I_EGLk"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Новости', 'Oton.Market🔵']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Мероприятия 2020✈', 'Маркетинг план📊']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Нужна помощь💡']])
    msg = bot.send_message(m.chat.id, 'Добро пожаловать в главное меню!',
                     reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)



def name(m):
    if m.text == 'Новости':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Действующие акции📉']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезные видео📹']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Будьте в курсе всех новостей!',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, second)

    elif m.text == 'Oton.Market🔵':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['ParkeS🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['BIOCOM🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Продукция https://oton.market!',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, second)

    elif m.text == 'Мероприятия 2020✈':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Предстоящие offline ивенты👜']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Расписание online форумов📍']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Продукция https://oton.market!',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, second)

    # elif m.text == 'Маркетинг план📊':
    #     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     keyboard.add(*[types.KeyboardButton(advert) for advert in ['Предстоящие offline ивенты👜']])
    #     keyboard.add(*[types.KeyboardButton(advert) for advert in ['Расписание online форумов📍']])
    #     keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])
    #
    #     bot.send_message(m.chat.id, 'Продукция https://oton.market!',
    #                      reply_markup=keyboard)
    #       bot.register_next_step_handler(msg, second)

    elif m.text == 'Нужна помощь💡':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезная информация🗂']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Финансы💳']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Обучение📚']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Продукция https://oton.market!',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, second)



def second(m):
    if m.text == '⬅️В главное меню':
        start(m)

    elif m.text == 'Полезные видео📹':
        msg = bot.send_message(m.chat.id, 'Анатолий Илле. Как построить большую организацию? Техника 4 шага - https://www.youtube.com/watch?v=7epTluPh428&t=4s')

        msg = bot.send_message(m.chat.id, 'Анатолий Илле о криптовалютах и как действовать именно сейчас! - https://www.youtube.com/watch?v=nxm3joAsru8&t=1s')


bot.polling(none_stop=True)
