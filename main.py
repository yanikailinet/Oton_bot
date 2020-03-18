import telebot
from telebot import types
import sales
import events
import marketplace
import helpme
import topvideo



token = "703356954:AAHnGvHB0KE-mpkkH_pWwOBHItxu8I_EGLk"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['🇷🇺Русский']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['🇬🇧English']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['🇹🇷Turkish']])
    msg = bot.send_message(m.chat.id, '👋🏼Привет! Меня зовут OTON. Я - твой личный помощник в экосистеме OTON и сообществе Easy Business Community! Буду рад помочь тебе разобраться в системе, рассказать о новостях, поделиться полезными материалами и как можно быстрее привести тебя к желаемой цели. Давай познакомимся поближе! Чтобы начать общение - просто активируй меня, выбрав свой язык! Ну что, поехали?! ',
                           reply_markup=keyboard)
    bot.register_next_step_handler(msg, starter)


def starter(m):
    if m.text == '🇷🇺Русский':
        startwo(m)

    elif m.text == '🇬🇧English':
       starthree(m)

    elif m.text == '🇹🇷Turkish':
       startfour(m)

    else:
        starter(m)



@bot.message_handler(commands=["startwo"])
def startwo(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Новости📨', 'Oton.Market🔵']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Мероприятия 2020✈', 'Узнай о нас🔎']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Телеграм-чаты📱', 'ТОП видео💾', 'Нужна помощь💡']])
    msg = bot.send_message(m.chat.id, 'Добро пожаловать в главное меню!',
                           reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)


def name(m):
    if m.text == 'Новости📨':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Действующие акции📉']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Актуальные видео📹']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Будьте в курсе всех новостей!',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, news)

    elif m.text == 'Oton.Market🔵':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['ParkeS🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['BIOCOM🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['LOSEV Formulas🧬']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['VITA-RA🔬']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id,
                               'OTON.Market - сервисы и услуги для индустрии сетевого маркетинга и прямых продаж, инновационные физические, цифровые, информационные, образовательные, развлекательные и финтехпродукты.  Абсолютная прозрачность взаимодействия между всеми участниками экосистемы OTON на максимально выгодных условиях.'  + "\n" + '🔵 https://oton.market 🔵',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, oton)

    elif m.text == 'Мероприятия 2020✈':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Предстоящие offline ивенты👜']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Расписание online форумов📍']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Как это было🎥']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Мероприятия',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, event)

    elif m.text == 'Узнай о нас🔎':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔑Бизнес']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['📚Образование']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔵Материалы']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, '🔵Тебя приветствует Бот Экосистемы OTON и сообщества Easy Business! Я помогу разобраться в системе. Чтобы узнать, как построить прибыльный бизнес и получать доход уже в первые недели работы - перейди по ссылке.  У меня есть что тебе предложить, чтобы ты достиг желаемого в любой сфере жизни на максимальной скорости! ',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, about)

    elif m.text == 'Телеграм-чаты📱':
        msg = bot.send_message(m.chat.id, '🗒 ПОДБОРКА TELEGRAM-ЧАТОВ КУРСОВ И СПИКЕРОВ EASY BUSINESS COMMUNITY'  + "\n" + "\n" + 'https://telegra.ph/Telegram-chaty-kursov-i-spikerov-Easy-Business-Community-06-19' )
        bot.register_next_step_handler(msg, name)

    elif m.text == 'ТОП видео💾':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['👨🏻‍💻Бизнес']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['💆🏼‍Здоровье и красота']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['👆🏼Интересное']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id,
                             '💾Здесь вы сможете найти материалы ТОП-спикеров нашего сообщества на интересующие Вас темы. Используйте бесплатный контент - подарки от спикеров, чтобы ваши партнеры, потенциальные и активные клиенты получили максимум пользы, а также рекомендуйте проходить полное обучение, предоставляя свои реферальные ссылки на курсы или предлагая пройти регистрацию и активировать пакет доступа, соответствующий курсу.',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, video)



    elif m.text == 'Нужна помощь💡':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезная информация🗂']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Финансы💳']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Обучение📚']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Тех. поддержка',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, help)

    else:
        startwo(m)




# БЛОК НОВОСТИ

def news(m):
    if m.text == 'Действующие акции📉':
        msg = bot.send_message(m.chat.id, sales.sale1)
        bot.register_next_step_handler(msg, news2)


    elif m.text == 'Актуальные видео📹':
        msg = bot.send_message(m.chat.id, 'https://telegra.ph/Aktualnye-video-Smotret-vsem-03-06')
        bot.register_next_step_handler(msg, news2)

    if m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


def news2(m):
    if m.text == 'Действующие акции📉':
        msg = bot.send_message(m.chat.id, sales.sale1)
        bot.register_next_step_handler(msg, news2)

    elif m.text == 'Актуальные видео📹':

        msg = bot.send_message(m.chat.id, 'https://telegra.ph/Aktualnye-video-Smotret-vsem-03-06')

        bot.register_next_step_handler(msg, news2)

    if m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


# БЛОК НОВОСТИ


# БЛОК МЕРОПРИЯТИЙ


def event(m):
    if m.text == 'Предстоящие offline ивенты👜':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2)

    elif m.text == 'Расписание online форумов📍':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2)

    elif m.text == 'Как это было🎥':

        msg = bot.send_message(m.chat.id, 'https://telegra.ph/EVENTS-Otchetnye-video-03-06')
        bot.register_next_step_handler(msg, event2)



    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


def event2(m):
    if m.text == 'Предстоящие offline ивенты👜':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2)

    elif m.text == 'Расписание online форумов📍':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2)

    elif m.text == 'Как это было🎥':

        msg = bot.send_message(m.chat.id, 'https://telegra.ph/EVENTS-Otchetnye-video-03-06')
        bot.register_next_step_handler(msg, event2)

    elif m.text == '⬅️В главное меню':
        startwo(m)


# БЛОК МЕРОПРИЯТИЙ


# БЛОК МАРКЕТПЛЭЙС


def oton(m):
    if m.text == 'ParkeS🧤':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезные видео о ParkeS🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Как купить ParkeS🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, marketplace.parkes,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.parkes2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonpar)


    elif m.text == 'BIOCOM🌱':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезные видео о BIOCOM🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Как купить BIOCOM🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, marketplace.biocom,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.biocom2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonbio)


    elif m.text == 'LOSEV Formulas🧬':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезные видео о LOSEV🧬']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Как купить LOSEV🧬']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, marketplace.losev,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.losev2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonlosev)


    elif m.text == 'VITA-RA🔬':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезные видео о VITA-RA🔬 ']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Как купить VITA-RA🔬']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, marketplace.vitara,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.vitara2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonvita)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)



def otonpar(m):
    if m.text == 'Полезные видео о ParkeS🧤':
        msg = bot.send_message(m.chat.id, marketplace.parkesvideo)
        bot.register_next_step_handler(msg, otonpar2)

    elif m.text == 'Как купить ParkeS🧤':
        msg = bot.send_message(m.chat.id, '🧤Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/parkes 🔵')
        bot.register_next_step_handler(msg, otonpar2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)

def otonpar2(m):
    if m.text == 'Полезные видео о ParkeS🧤':
        msg = bot.send_message(m.chat.id, marketplace.parkesvideo)
        bot.register_next_step_handler(msg, otonpar2)

    elif m.text == 'Как купить ParkeS🧤':
        msg = bot.send_message(m.chat.id, '🧤Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/parkes 🔵')
        bot.register_next_step_handler(msg, otonpar2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


def otonbio(m):
    if m.text == 'Полезные видео о BIOCOM🌱':
        msg = bot.send_message(m.chat.id, marketplace.biocomvideo)
        bot.register_next_step_handler(msg, otonbio2)

    elif m.text == 'Как купить BIOCOM🌱':
        msg = bot.send_message(m.chat.id, '🌱Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/biocom 🔵')
        bot.register_next_step_handler(msg, otonbio2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)

def otonbio2(m):
    if m.text == 'Полезные видео о BIOCOM🌱':
        msg = bot.send_message(m.chat.id, marketplace.biocomvideo)
        bot.register_next_step_handler(msg, otonbio2)

    elif m.text == 'Как купить BIOCOM🌱':
        msg = bot.send_message(m.chat.id,
                               '🌱Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты LOSEV Formulas' + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/losev 🔵')

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


def otonlosev(m):
    if m.text == 'Полезные видео о LOSEV🧬':
        msg = bot.send_message(m.chat.id, marketplace.losevvideo)
        bot.register_next_step_handler(msg, otonlosev2)

    elif m.text == 'Как купить LOSEV🧬':
        msg = bot.send_message(m.chat.id,
                               '🌱Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты LOSEV Formulas' + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/losev 🔵')
        bot.register_next_step_handler(msg, otonlosev2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


def otonlosev2(m):
    if m.text == 'Полезные видео о LOSEV🧬':
        msg = bot.send_message(m.chat.id, marketplace.losevvideo)
        bot.register_next_step_handler(msg, otonlosev2)

    elif m.text == 'Как купить LOSEV🧬':
        msg = bot.send_message(m.chat.id,
                               '🌱Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS' + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/biocom 🔵')
        bot.register_next_step_handler(msg, otonlosev2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


def otonvita(m):
    if m.text == 'Полезные видео о VITA-RA🔬':
        msg = bot.send_message(m.chat.id, marketplace.vitaravideo)
        bot.register_next_step_handler(msg, otonvita2)

    elif m.text == 'Как купить VITA-RA🔬':
        msg = bot.send_message(m.chat.id, '🔬Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/vita-ra 🔵')
        bot.register_next_step_handler(msg, otonvita2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)

def otonvita2(m):
    if m.text == 'Полезные видео о VITA-RA🔬':
        msg = bot.send_message(m.chat.id, marketplace.vitaravideo)
        bot.register_next_step_handler(msg, otonvita2)

    elif m.text == 'Как купить VITA-RA🔬':
        msg = bot.send_message(m.chat.id, '🔬Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/vita-ra 🔵')
        bot.register_next_step_handler(msg, otonvita2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


# БЛОК МАРКЕТПЛЭЙС


# БЛОК О КОМПАНИИ
def about(m):
    if m.text == '🔑Бизнес':

        msg = bot.send_message(m.chat.id, '🔑Бизнес в экосистеме OTON - создай свой собственный, технологичный и прибыльный бизнес! Все о преимуществах и возможностях ты найдешь в презентации "Бизнес под ключ" а еще больше тебе расскажет тот, кто поделился с тобой ссылкой на этот бот!'  + "\n" + "\n" +  '📌Презентация "Бизнес под ключ - https://oton.org/media/1.%20Presentation%20(RU).pdf?013513c2' )
        msg = bot.send_message(m.chat.id,'📌Видео презентация - https://www.youtube.com/watch?v=3RIvV_fRYVs')
        bot.register_next_step_handler(msg, about2)

    elif m.text == '📚Образование':

        msg = bot.send_message(m.chat.id, '📚Знания в чистом виде: макисмум практики, ТОП-спикеры мирового уровня, курсы, вебинары, марафоны темам из основных сфер жизни. Обучайся, развивайся и становись лучшей версией себя!'  + "\n" + "\n" + '📌Курсы - https://easy-bizzi.com/ru/courses'  + "\n" + '📌Вебинары - https://easy-bizzi.com/ru/webinars')
        bot.register_next_step_handler(msg, about2)

    elif m.text == '🔵Материалы':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔵Методичные материалы OTON']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔵Экосистема OTON']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔵Бизнес под ключ']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔵Видеоинструкции']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, "📥Все инструменты для создания бизнеса и работы с командой всегда под рукой! Осталось только скачать...",
                               reply_markup=keyboard)

        bot.register_next_step_handler(msg, aboutmaterials)



    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


def about2(m):
    if m.text == '🔑Бизнес':

        msg = bot.send_message(m.chat.id, '🔑Бизнес в экосистеме OTON - создай свой собственный, технологичный и прибыльный бизнес! Все о преимуществах и возможностях ты найдешь в презентации "Бизнес под ключ" а еще больше тебе расскажет тот, кто поделился с тобой ссылкой на этот бот!'  + "\n" + "\n" +  '📌Презентация "Бизнес под ключ - https://oton.org/media/1.%20Presentation%20(RU).pdf?013513c2' )
        msg = bot.send_message(m.chat.id,'📌Видео презентация - https://www.youtube.com/watch?v=3RIvV_fRYVs')
        bot.register_next_step_handler(msg, about2)

    elif m.text == '📚Образование':

        msg = bot.send_message(m.chat.id, '📚Знания в чистом виде: макисмум практики, ТОП-спикеры мирового уровня, курсы, вебинары, марафоны темам из основных сфер жизни. Обучайся, развивайся и становись лучшей версией себя!'   + "\n" + "\n" + '📌Курсы - https://easy-bizzi.com/ru/courses'  + "\n" + '📌Вебинары - https://easy-bizzi.com/ru/webinars')
        bot.register_next_step_handler(msg, about2)

    elif m.text == '🔵Материалы':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔵Методичные материалы OTON']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔵Экосистема OTON']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔵Бизнес под ключ']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔵Видеоинструкции']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id,
                               "📥Все инструменты для создания бизнеса и работы с командой всегда под рукой! Осталось только скачать...",
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, aboutmaterials)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)

def aboutmaterials(m):
    if m.text == '🔵Методичные материалы OTON':

        msg = bot.send_message(m.chat.id,'https://telegra.ph/Metodichnye-materialy-OTON-03-05')
        bot.register_next_step_handler(msg, aboutmaterials2)

    elif m.text == '🔵Экосистема OTON':

        msg = bot.send_message(m.chat.id,'https://telegra.ph/EHkosistema-OTON-03-05')
        bot.register_next_step_handler(msg, aboutmaterials2)

    elif m.text == '🔵Бизнес под ключ':

        msg = bot.send_message(m.chat.id,'https://telegra.ph/Biznes-pod-klyuch-03-05')
        bot.register_next_step_handler(msg, aboutmaterials2)

    elif m.text == '🔵Видеоинструкции':

        msg = bot.send_message(m.chat.id, 'https://telegra.ph/Videoinstrukcii-03-06')
        bot.register_next_step_handler(msg, aboutmaterials2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


def aboutmaterials2(m):
    if m.text == '🔵Методичные материалы OTON':

        msg = bot.send_message(m.chat.id, 'https://telegra.ph/Metodichnye-materialy-OTON-03-05')
        bot.register_next_step_handler(msg, aboutmaterials2)

    elif m.text == '🔵Экосистема OTON':

        msg = bot.send_message(m.chat.id, 'https://telegra.ph/EHkosistema-OTON-03-05')
        bot.register_next_step_handler(msg, aboutmaterials2)

    elif m.text == '🔵Бизнес под ключ':

        msg = bot.send_message(m.chat.id, 'https://telegra.ph/Biznes-pod-klyuch-03-05')
        bot.register_next_step_handler(msg, aboutmaterials2)

    elif m.text == '🔵Видеоинструкции':

        msg = bot.send_message(m.chat.id, 'https://telegra.ph/Videoinstrukcii-03-06')
        bot.register_next_step_handler(msg, aboutmaterials2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)




# БЛОК О КОМПАНИИ

#БЛОК ВИДЕО

def video(m):
    if m.text == '👨🏻‍💻Бизнес':

        msg = bot.send_message(m.chat.id, topvideo.biz1)

        bot.register_next_step_handler(msg, video2)

    elif m.text == '💆🏼‍Здоровье и красота':

        msg = bot.send_message(m.chat.id, topvideo.hel1)

        bot.register_next_step_handler(msg, video2)

    elif m.text == '👆🏼Интересное':

        msg = bot.send_message(m.chat.id, topvideo.int1)

        bot.register_next_step_handler(msg, video2)


    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)

def video2(m):
    if m.text == '👨🏻‍💻Бизнес':

        msg = bot.send_message(m.chat.id, topvideo.biz1)

        bot.register_next_step_handler(msg, video2)

    elif m.text == '💆🏼‍Здоровье и красота':

        msg = bot.send_message(m.chat.id, topvideo.hel1)

        bot.register_next_step_handler(msg, video2)

    elif m.text == '👆🏼Интересное':

        msg = bot.send_message(m.chat.id, topvideo.int1)
 
        bot.register_next_step_handler(msg, video2)


    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)

#БЛОК ВИДЕО


# БЛОК ТЕХПОДДЕРЖКИ

def help(m):
    if m.text == 'Полезная информация🗂':

        msg = bot.send_message(m.chat.id, helpme.helpinfo)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2)

    elif m.text == 'Финансы💳':

        msg = bot.send_message(m.chat.id, helpme.helpfinance)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2)

    elif m.text == 'Обучение📚':

        msg = bot.send_message(m.chat.id, helpme.helplearn)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2)


    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)


def help2(m):
    if m.text == 'Полезная информация🗂':

        msg = bot.send_message(m.chat.id, helpme.helpinfo)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2)

    elif m.text == 'Финансы💳':

        msg = bot.send_message(m.chat.id, helpme.helpfinance)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2)

    elif m.text == 'Обучение📚':

        msg = bot.send_message(m.chat.id, helpme.helplearn)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2)

    elif m.text == '⬅️В главное меню':
        startwo(m)

    else:
        startwo(m)
# БЛОК ТЕХПОДДЕРЖКИ


# АНГЛИЙСКИЙ
@bot.message_handler(commands=["starthree"])
def starthree(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Новости📨', 'Oton.Market🔵']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Мероприятия 2020✈', 'Узнай о нас🔎']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Телеграм-чаты📱', 'Нужна помощь💡']])
    msg = bot.send_message(m.chat.id, 'Добро пожаловать в главное меню!',
                           reply_markup=keyboard)
    bot.register_next_step_handler(msg, nameeng)


def nameeng(m):
    if m.text == 'Новости📨':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Действующие акции📉']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезные видео📹']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Будьте в курсе всех новостей!',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, newseng)

    elif m.text == 'Oton.Market🔵':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['ParkeS🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['BIOCOM🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['VITA-RA🔬']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id,
                               'OTON.Market - сервисы и услуги для индустрии сетевого маркетинга и прямых продаж, инновационные физические, цифровые, информационные, образовательные, развлекательные и финтехпродукты.  Абсолютная прозрачность взаимодействия между всеми участниками экосистемы OTON на максимально выгодных условиях.'  + "\n" + '🔵 https://oton.market 🔵',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otoneng)

    elif m.text == 'Мероприятия 2020✈':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Предстоящие offline ивенты👜']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Расписание online форумов📍']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Мероприятия',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, eventeng)

    elif m.text == 'Узнай о нас🔎':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔑Бизнес']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['📚Образование']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, '🔵Тебя приветствует Бот Экосистемы OTON и сообщества Easy Business! Я помогу разобраться в системе. Чтобы узнать, как построить прибыльный бизнес и получать доход уже в первые недели работы - перейди по ссылке.  У меня есть что тебе предложить, чтобы ты достиг желаемого в любой сфере жизни на максимальной скорости! ',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, abouteng)

    elif m.text == 'Телеграм-чаты📱':
        msg = bot.send_message(m.chat.id, '🗒 ПОДБОРКА TELEGRAM-ЧАТОВ КУРСОВ И СПИКЕРОВ EASY BUSINESS COMMUNITY'  + "\n" + "\n" + 'https://telegra.ph/Telegram-chaty-kursov-i-spikerov-Easy-Business-Community-06-19' )
        bot.register_next_step_handler(msg, nameeng)

    elif m.text == 'Нужна помощь💡':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезная информация🗂']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Финансы💳']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Обучение📚']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, 'Тех. поддержка',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, helpeng)


# БЛОК НОВОСТИ

def newseng(m):
    if m.text == 'Действующие акции📉':
        msg = bot.send_message(m.chat.id, sales.sale1)
        msg = bot.send_message(m.chat.id, sales.sale2)
        msg = bot.send_message(m.chat.id, sales.sale3)
        msg = bot.send_message(m.chat.id, sales.sale4)
        bot.register_next_step_handler(msg, news2eng)


    elif m.text == 'Полезные видео📹':
        msg = bot.send_message(m.chat.id,
                               'Анатолий Илле. Как построить большую организацию? Техника 4 шага - https://www.youtube.com/watch?v=7epTluPh428&t=4s')
        msg = bot.send_message(m.chat.id,
                               'Анатолий Илле о криптовалютах и как действовать именно сейчас! - https://www.youtube.com/watch?v=nxm3joAsru8&t=1s')
        bot.register_next_step_handler(msg, news2eng)

    if m.text == '⬅️В главное меню':
        starthree(m)


def news2eng(m):
    if m.text == 'Действующие акции📉':
        msg = bot.send_message(m.chat.id, sales.sale1)

        bot.register_next_step_handler(msg, news2eng)

    elif m.text == 'Полезные видео📹':
        msg = bot.send_message(m.chat.id,
                               'Анатолий Илле. Как построить большую организацию? Техника 4 шага - https://www.youtube.com/watch?v=7epTluPh428&t=4s')
        msg = bot.send_message(m.chat.id,
                               'Анатолий Илле о криптовалютах и как действовать именно сейчас! - https://www.youtube.com/watch?v=nxm3joAsru8&t=1s')
        bot.register_next_step_handler(msg, news2eng)

    if m.text == '⬅️В главное меню':
        starthree(m)


# БЛОК НОВОСТИ


# БЛОК МЕРОПРИЯТИЙ


def eventeng(m):
    if m.text == 'Предстоящие offline ивенты👜':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2)

    elif m.text == 'Расписание online форумов📍':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)


def event2eng(m):
    if m.text == 'Предстоящие offline ивенты👜':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2eng)

    elif m.text == 'Расписание online форумов📍':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)


# БЛОК МЕРОПРИЯТИЙ


# БЛОК МАРКЕТПЛЭЙС


def otoneng(m):
    if m.text == 'ParkeS🧤':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезные видео о ParkeS🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Как купить ParkeS🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, marketplace.parkes,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.parkes2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonpareng)


    elif m.text == 'BIOCOM🌱':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезные видео о BIOCOM🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Как купить BIOCOM🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, marketplace.biocom,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.biocom2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonbioeng)

    elif m.text == 'VITA-RA🔬':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Полезные видео о VITA-RA🔬 ']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Как купить VITA-RA🔬']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️В главное меню']])

        msg = bot.send_message(m.chat.id, marketplace.vitara,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.vitara2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonvitaeng)

    elif m.text == '⬅️В главное меню':
        starthree(m)




def otonpareng(m):
    if m.text == 'Полезные видео о ParkeS🧤':
        msg = bot.send_message(m.chat.id, marketplace.parkesvideo)
        bot.register_next_step_handler(msg, otonpar2eng)

    elif m.text == 'Как купить ParkeS🧤':
        msg = bot.send_message(m.chat.id, '🧤Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/parkes 🔵')
        bot.register_next_step_handler(msg, otonpar2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)

def otonpar2eng(m):
    if m.text == 'Полезные видео о ParkeS🧤':
        msg = bot.send_message(m.chat.id, marketplace.parkesvideo)
        bot.register_next_step_handler(msg, otonpar2eng)

    elif m.text == 'Как купить ParkeS🧤':
        msg = bot.send_message(m.chat.id, '🧤Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/parkes 🔵')
        bot.register_next_step_handler(msg, otonpar2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)


def otonbioeng(m):
    if m.text == 'Полезные видео о BIOCOM🌱':
        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, otonbio2eng)

    elif m.text == 'Как купить BIOCOM🌱':
        msg = bot.send_message(m.chat.id, '🌱Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/biocom 🔵')
        bot.register_next_step_handler(msg, otonbio2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)

def otonbio2eng(m):
    if m.text == 'Полезные видео о BIOCOM🌱':
        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, otonbio2eng)

    elif m.text == 'Как купить BIOCOM🌱':
        msg = bot.send_message(m.chat.id, '🌱Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/biocom 🔵')
        bot.register_next_step_handler(msg, otonbio2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)


def otonvitaeng(m):
    if m.text == 'Полезные видео о VITA-RA🔬':
        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, otonvita2eng)

    elif m.text == 'Как купить VITA-RA🔬':
        msg = bot.send_message(m.chat.id, '🔬Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/vita-ra 🔵')
        bot.register_next_step_handler(msg, otonvita2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)

def otonvita2eng(m):
    if m.text == 'Полезные видео о VITA-RA🔬':
        msg = bot.send_message(m.chat.id, 'Hi')
        bot.register_next_step_handler(msg, otonvita2eng)

    elif m.text == 'Как купить VITA-RA🔬':
        msg = bot.send_message(m.chat.id, '🔬Перейдите по ссылке на OTON.Market, введите свой пароль и логин для входа в систему, чтобы приобрести продукты ParkeS'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/vita-ra 🔵')
        bot.register_next_step_handler(msg, otonvita2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)





# def oton3(m):
#     if m.text == 'Назад':
#         oton(m)

# БЛОК МАРКЕТПЛЭЙС


# БЛОК О КОМПАНИИ
def abouteng(m):
    if m.text == '🔑Бизнес':

        msg = bot.send_message(m.chat.id, '🔑Бизнес в экосистеме OTON - создай свой собственный, технологичный и прибыльный бизнес! Все о преимуществах и возможностях ты найдешь в презентации "Бизнес под ключ" а еще больше тебе расскажет тот, кто поделился с тобой ссылкой на этот бот!'  + "\n" + "\n" +  '📌Презентация "Бизнес под ключ - https://oton.org/media/1.%20Presentation%20(RU).pdf?013513c2' )
        msg = bot.send_message(m.chat.id,'📌Видео презентация - https://www.youtube.com/watch?v=3RIvV_fRYVs')
        bot.register_next_step_handler(msg, about2eng)

    elif m.text == '📚Образование':

        msg = bot.send_message(m.chat.id, '📚Знания в чистом виде: макисмум практики, ТОП-спикеры мирового уровня, курсы, вебинары, марафоны темам из основных сфер жизни. Обучайся, развивайся и становись лучшей версией себя!'  + "\n" + "\n" + '📌Курсы - https://easy-bizzi.com/ru/courses'  + "\n" + '📌Вебинары - https://easy-bizzi.com/ru/webinars')
        bot.register_next_step_handler(msg, about2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)


def about2eng(m):
    if m.text == '🔑Бизнес':

        msg = bot.send_message(m.chat.id, '🔑Бизнес в экосистеме OTON - создай свой собственный, технологичный и прибыльный бизнес! Все о преимуществах и возможностях ты найдешь в презентации "Бизнес под ключ" а еще больше тебе расскажет тот, кто поделился с тобой ссылкой на этот бот!'  + "\n" + "\n" +  '📌Презентация "Бизнес под ключ - https://oton.org/media/1.%20Presentation%20(RU).pdf?013513c2' )
        msg = bot.send_message(m.chat.id,'📌Видео презентация - https://www.youtube.com/watch?v=3RIvV_fRYVs')
        bot.register_next_step_handler(msg, about2eng)

    elif m.text == '📚Образование':

        msg = bot.send_message(m.chat.id, '📚Знания в чистом виде: макисмум практики, ТОП-спикеры мирового уровня, курсы, вебинары, марафоны темам из основных сфер жизни. Обучайся, развивайся и становись лучшей версией себя!'   + "\n" + "\n" + '📌Курсы - https://easy-bizzi.com/ru/courses'  + "\n" + '📌Вебинары - https://easy-bizzi.com/ru/webinars')
        bot.register_next_step_handler(msg, about2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)




# БЛОК О КОМПАНИИ


# БЛОК ТЕХПОДДЕРЖКИ

def helpeng(m):
    if m.text == 'Полезная информация🗂':

        msg = bot.send_message(m.chat.id, helpme.helpinfo)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2eng)

    elif m.text == 'Финансы💳':

        msg = bot.send_message(m.chat.id, helpme.helpfinance)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2eng)

    elif m.text == 'Обучение📚':

        msg = bot.send_message(m.chat.id, helpme.helplearn)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2eng)


    elif m.text == '⬅️В главное меню':
        starthree(m)


def help2eng(m):
    if m.text == 'Полезная информация🗂':

        msg = bot.send_message(m.chat.id, helpme.helpinfo)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2eng)

    elif m.text == 'Финансы💳':

        msg = bot.send_message(m.chat.id, helpme.helpfinance)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2eng)

    elif m.text == 'Обучение📚':

        msg = bot.send_message(m.chat.id, helpme.helplearn)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2eng)

    elif m.text == '⬅️В главное меню':
        starthree(m)
# БЛОК ТЕХПОДДЕРЖКИ

# АНГЛИЙСКИЙ

#ТУРЕЦКИЙ

@bot.message_handler(commands=["startfour"])
def startfour(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Haberler📨', 'Oton.Market🔵']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Etkinlikler 2020✈', 'Bizi tanıyın🔎']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Telegram-sohbetler📱', 'En iyi video💾', 'Yardıma ihtiyacınız var💡']])
    msg = bot.send_message(m.chat.id, 'Ana menüye hoş geldiniz!',
                           reply_markup=keyboard)
    bot.register_next_step_handler(msg, nametur)


def nametur(m):
    if m.text == 'Haberler📨':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Mevcut hisse senetleri📉']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Faydalı videolar📹']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️Ana Menü']])

        msg = bot.send_message(m.chat.id, 'Tüm haberleri takip edin!',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, newstur)

    elif m.text == 'Oton.Market🔵':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['ParkeS🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['BIOCOM🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['VITA-RA🔬']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️️Ana Menü']])

        msg = bot.send_message(m.chat.id,
                               'OTON.Market - ağ pazarlama ve doğrudan satış, yenilikçi fiziksel, dijital, bilgilendirici, eğitim, eğlence ve fintech ürünleri endüstrisi hizmetleri içindir. OTON ekosisteminin tüm katılımcıları arasında en uygun koşullarda etkileşimin mutlak şeffaflığı vardır.'  + "\n" + '🔵 https://oton.market 🔵',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otontur)

    elif m.text == 'Etkinlikler 2020✈':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Önümüzdeki offline etkinlikler👜']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Önümüzdeki online etkinlikler📍']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️Ana Menü']])

        msg = bot.send_message(m.chat.id, 'Мероприятия',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, eventtur)

    elif m.text == 'Bizi tanıyın🔎':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['🔑İşletme']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['📚Eğitim']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️Ana Menü']])

        msg = bot.send_message(m.chat.id, '🔵OTON Ekosistem Botuna ve Easy Business topluluğuna  Hoş Geldiniz! Ben sistemi anlamaya yardımcı olacağım.Karlı bir iş kurmayı ve işin ilk haftalarında gelir elde etmeyi öğrenmek için bağlantıyı tıklayın. Size sunabileceğim bir şey var, böylece yaşamın herhangi bir alanında maksimum hızda istediğinizi elde edebilirsiniz!',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, abouttur)

    elif m.text == 'Telegram-sohbetler📱':
        msg = bot.send_message(m.chat.id,
                               '🗒 ПОДБОРКА TELEGRAM-ЧАТОВ КУРСОВ И СПИКЕРОВ EASY BUSINESS COMMUNITY' + "\n" + "\n" + 'https://telegra.ph/Telegram-chaty-kursov-i-spikerov-Easy-Business-Community-06-19')
        bot.register_next_step_handler(msg, nametur)

    elif m.text == 'En iyi video💾':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['👨🏻‍💻İşletme']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['💆🏼Sağlık ve Güzellik']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['👆🏼ilginç']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️Ana Menü']])

        msg = bot.send_message(m.chat.id,
                             '💾Burada ilgimizi çeken konularda topluluğumuzun TOP konuşmacılarının materyallerini bulabilirsiniz!',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, videotur)


    elif m.text == 'Yardıma ihtiyacınız var💡':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Faydalı bilgiler🗂']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Finans💳']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Eğitim📚']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️Ana Menü']])

        msg = bot.send_message(m.chat.id, 'Тех. поддержка',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, helptur)


# БЛОК НОВОСТИ

def newstur(m):
    if m.text == 'Mevcut hisse senetleri📉':
        msg = bot.send_message(m.chat.id, sales.sale1)

        bot.register_next_step_handler(msg, news2tur)


    elif m.text == 'Faydalı videolar📹':
        msg = bot.send_message(m.chat.id,
                               'Анатолий Илле. Как построить большую организацию? Техника 4 шага - https://www.youtube.com/watch?v=7epTluPh428&t=4s')
        msg = bot.send_message(m.chat.id,
                               'Анатолий Илле о криптовалютах и как действовать именно сейчас! - https://www.youtube.com/watch?v=nxm3joAsru8&t=1s')
        bot.register_next_step_handler(msg, news2tur)

    if m.text == '⬅️Ana Menü':
        startfour(m)


def news2tur(m):
    if m.text == 'Mevcut hisse senetleri📉':
        msg = bot.send_message(m.chat.id, sales.sale1)

        bot.register_next_step_handler(msg, news2tur)

    elif m.text == 'Faydalı videolar📹':
        msg = bot.send_message(m.chat.id,
                               'Анатолий Илле. Как построить большую организацию? Техника 4 шага - https://www.youtube.com/watch?v=7epTluPh428&t=4s')
        msg = bot.send_message(m.chat.id,
                               'Анатолий Илле о криптовалютах и как действовать именно сейчас! - https://www.youtube.com/watch?v=nxm3joAsru8&t=1s')
        bot.register_next_step_handler(msg, news2tur)

    if m.text == '⬅️Ana Menü':
        startfour(m)


# БЛОК НОВОСТИ


# БЛОК МЕРОПРИЯТИЙ


def eventtur(m):
    if m.text == 'Önümüzdeki offline etkinlikler👜':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2)

    elif m.text == 'Önümüzdeki online etkinlikle📍':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)


def event2tur(m):
    if m.text == 'Önümüzdeki offline etkinlikler👜':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2tur)

    elif m.text == 'Önümüzdeki online etkinlikle📍':

        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, event2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)


# БЛОК МЕРОПРИЯТИЙ


# БЛОК МАРКЕТПЛЭЙС


def otontur(m):
    if m.text == 'ParkeS🧤':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['ParkeS hakkında faydalı videolar🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Nasıl alınır ParkeS🧤']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️Ana Menü']])

        msg = bot.send_message(m.chat.id, marketplace.parkes,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.parkes2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonpartur)


    elif m.text == 'BIOCOM🌱':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['BIOCOM hakkında faydalı videolar🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Nasıl alınır BIOCOM🌱']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️Ana Menü']])

        msg = bot.send_message(m.chat.id, marketplace.biocom,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.biocom2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonbiotur)

    elif m.text == 'VITA-RA🔬':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['VITA-RA hakkında faydalı videolar🔬 ']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Nasıl alınır VITA-RA🔬']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['⬅️Ana Menü']])

        msg = bot.send_message(m.chat.id, marketplace.vitara,
                               reply_markup=keyboard)
        msg = bot.send_message(m.chat.id, marketplace.vitara2,
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, otonvitatur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)




def otonpartur(m):
    if m.text == 'ParkeS hakkında faydalı videolar🧤':
        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, otonpar2tur)

    elif m.text == 'Nasıl alınır ParkeS🧤':
        msg = bot.send_message(m.chat.id, '🧤OTON.Market bağlantısını takip edin, şifrenizi girin ve ParkeS ürünlerini satın almak için oturum açın.'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/parkes 🔵')
        bot.register_next_step_handler(msg, otonpar2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)

def otonpar2tur(m):
    if m.text == 'ParkeS hakkında faydalı videolar🧤':
        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, otonpar2tur)

    elif m.text == 'Nasıl alınır ParkeS🧤':
        msg = bot.send_message(m.chat.id, '🧤OTON.Market bağlantısını takip edin, şifrenizi girin ve ParkeS ürünlerini satın almak için oturum açın.'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/parkes 🔵')
        bot.register_next_step_handler(msg, otonpar2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)


def otonbiotur(m):
    if m.text == 'BIOCOM hakkında faydalı videolar🌱':
        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, otonbio2tur)

    elif m.text == 'Nasıl alınır BIOCOM🌱':
        msg = bot.send_message(m.chat.id, '🌱OTON.Market bağlantısını takip edin, şifrenizi girin ve BIOCOM ürünlerini satın almak için oturum açın.'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/biocom 🔵')
        bot.register_next_step_handler(msg, otonbio2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)

def otonbio2tur(m):
    if m.text == 'BIOCOM hakkında faydalı videolar🌱':
        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, otonbio2tur)

    elif m.text == 'Nasıl alınır BIOCOM🌱':
        msg = bot.send_message(m.chat.id, '🌱OTON.Market bağlantısını takip edin, şifrenizi girin ve BIOCOM ürünlerini satın almak için oturum açın.'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/biocom 🔵')
        bot.register_next_step_handler(msg, otonbio2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)


def otonvitatur(m):
    if m.text == 'VITA-RA hakkında faydalı videolar🔬':
        msg = bot.send_message(m.chat.id, 'Будет инфо')
        bot.register_next_step_handler(msg, otonvita2tur)

    elif m.text == 'Nasıl alınır VITA-RA🔬':
        msg = bot.send_message(m.chat.id, '🔬OTON.Market bağlantısını takip edin, şifrenizi girin ve VITA-RA ürünlerini satın almak için oturum açın.'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/vita-ra 🔵')
        bot.register_next_step_handler(msg, otonvita2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)

def otonvita2tur(m):
    if m.text == 'VITA-RA hakkında faydalı videolar🔬':
        msg = bot.send_message(m.chat.id, 'Hi')
        bot.register_next_step_handler(msg, otonvita2tur)

    elif m.text == 'Nasıl alınır VITA-RA🔬':
        msg = bot.send_message(m.chat.id, '🔬OTON.Market bağlantısını takip edin, şifrenizi girin ve VITA-RA ürünlerini satın almak için oturum açın.'  + "\n" + "\n" + '🔵 https://oton.market/ru/vendor/vita-ra 🔵')
        bot.register_next_step_handler(msg, otonvita2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)




# БЛОК МАРКЕТПЛЭЙС


# БЛОК О КОМПАНИИ
def abouttur(m):
    if m.text == '🔑İşletme':

        msg = bot.send_message(m.chat.id, '🔑OTON ekosisteminde kendi yüksek teknolojili ve karlı işinizi yaratın! "Anahtar Teslimi İş" sunumunda avantajlar ve fırsatlar hakkında her şeyi bulacaksınız ve bu botun bağlantısını sizinle paylaşan biri size daha fazlasını söyleyecektir!' )
        msg = bot.send_message(m.chat.id,'📌Video sunum - https://www.youtube.com/watch?v=3RIvV_fRYVs')
        bot.register_next_step_handler(msg, about2tur)

    elif m.text == '📚Eğitim':

        msg = bot.send_message(m.chat.id, '📚En saf haliyle bilgi: maksimum uygulama, dünya standartlarında en iyi konuşmacılar, kurslar, web seminerleri, çeşitli konularda maratonlar: reklam, pazarlama, iş, kişisel gelişim. Ayrıca, eğitim platformumuza sürekli olarak dersler eklenmektedir, daha sonra onay olarak bir meslek ve sertifika alabilirsiniz.Kendinizi eğitin, geliştirin ve kendinizin en iyi versiyonu olun!'  + "\n" + "\n" + '📌Курсы - https://easy-bizzi.com/ru/courses'  + "\n" + '📌Вебинары - https://easy-bizzi.com/ru/webinars')
        bot.register_next_step_handler(msg, about2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)


def about2tur(m):
    if m.text == '🔑İşletme':

        msg = bot.send_message(m.chat.id, '🔑OTON ekosisteminde kendi yüksek teknolojili ve karlı işinizi yaratın! "Anahtar Teslimi İş" sunumunda avantajlar ve fırsatlar hakkında her şeyi bulacaksınız ve bu botun bağlantısını sizinle paylaşan biri size daha fazlasını söyleyecektir!' )
        msg = bot.send_message(m.chat.id,'📌Video sunum - https://www.youtube.com/watch?v=3RIvV_fRYVs')
        bot.register_next_step_handler(msg, about2tur)

    elif m.text == '📚Eğitim':

        msg = bot.send_message(m.chat.id, '📚En saf haliyle bilgi: maksimum uygulama, dünya standartlarında en iyi konuşmacılar, kurslar, web seminerleri, çeşitli konularda maratonlar: reklam, pazarlama, iş, kişisel gelişim. Ayrıca, eğitim platformumuza sürekli olarak dersler eklenmektedir, daha sonra onay olarak bir meslek ve sertifika alabilirsiniz.Kendinizi eğitin, geliştirin ve kendinizin en iyi versiyonu olun!'  + "\n" + "\n" + '📌Курсы - https://easy-bizzi.com/ru/courses'  + "\n" + '📌Вебинары - https://easy-bizzi.com/ru/webinars')
        bot.register_next_step_handler(msg, about2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)




# БЛОК О КОМПАНИИ

#БЛОК ВИДЕО

def videotur(m):
    if m.text == '👨🏻‍💻İşletme':

        msg = bot.send_message(m.chat.id, 'Creating your own profitable, technological and safe business is easier than you think. How? To get started, just watch this video. I dare to suggest that you will like it because there has not been such an offer yet!')
        bot.register_next_step_handler(msg, video2tur)

    elif m.text == '💆🏼Sağlık ve Güzellik':

        msg = bot.send_message(m.chat.id, 'Наполнить курсами')
        bot.register_next_step_handler(msg, video2tur)

    elif m.text == '👆🏼ilginç':

        msg = bot.send_message(m.chat.id, 'Наполнить курсами')
        bot.register_next_step_handler(msg, video2tur)


    elif m.text == '⬅️Ana Menü':
        startfour(m)

def video2tur(m):
    if m.text == '👨🏻‍💻İşletme':

        msg = bot.send_message(m.chat.id, 'Creating your own profitable, technological and safe business is easier than you think. How? To get started, just watch this video. I dare to suggest that you will like it because there has not been such an offer yet!')
        bot.register_next_step_handler(msg, video2tur)

    elif m.text == '💆🏼Sağlık ve Güzellik':

        msg = bot.send_message(m.chat.id, 'Наполнить курсами')
        bot.register_next_step_handler(msg, video2tur)

    elif m.text == '👆🏼ilginç':

        msg = bot.send_message(m.chat.id, 'Наполнить курсами')
        bot.register_next_step_handler(msg, video2tur)


    elif m.text == '⬅️Ana Menü':
        startfour(m)

#БЛОК ВИДЕО



# БЛОК ТЕХПОДДЕРЖКИ

def helptur(m):
    if m.text == 'Полезная информация🗂':

        msg = bot.send_message(m.chat.id, helpme.helpinfo)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2tur)

    elif m.text == 'Финансы💳':

        msg = bot.send_message(m.chat.id, helpme.helpfinance)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2tur)

    elif m.text == 'Обучение📚':

        msg = bot.send_message(m.chat.id, helpme.helplearn)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2tur)


    elif m.text == '⬅️Ana Menü':
        startfour(m)


def help2tur(m):
    if m.text == 'Faydalı bilgiler🗂':

        msg = bot.send_message(m.chat.id, helpme.helpinfo)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2tur)

    elif m.text == 'Finans💳':

        msg = bot.send_message(m.chat.id, helpme.helpfinance)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2tur)

    elif m.text == 'Eğitim📚':

        msg = bot.send_message(m.chat.id, helpme.helplearn)
        msg = bot.send_message(m.chat.id, helpme.helpsup)
        bot.register_next_step_handler(msg, help2tur)

    elif m.text == '⬅️Ana Menü':
        startfour(m)
# БЛОК ТЕХПОДДЕРЖКИ


# #ТУРЕЦКИЙ




bot.polling(none_stop=True)
