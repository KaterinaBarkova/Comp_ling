# !pip install pyTelegramBotAPI
import telebot
from parse_news import parse_news
from preprocess_news import apply_prep
from classify_news import classify, get_news_by_cat
from datetime import datetime, timedelta

token = "1316919471:AAHNv3rQi6YRpTVC-u36QG9BgHZg-y6dT1w" # вставить свой токен
bot = telebot.TeleBot(token) 

keyboard = telebot.types.InlineKeyboardMarkup()

business_button = telebot.types.InlineKeyboardButton(text="Бизнес", callback_data='BUSINESS')
comedy_button = telebot.types.InlineKeyboardButton(text="Комедия", callback_data='COMEDY')
crime_button = telebot.types.InlineKeyboardButton(text="Криминал", callback_data='crime')
divorce_button = telebot.types.InlineKeyboardButton(text="Развод", callback_data='divorce')
food_drink_button = telebot.types.InlineKeyboardButton(text="Еда", callback_data='FOOD & DRINK')
home_living_button = telebot.types.InlineKeyboardButton(text="Дом", callback_data='home_living')
politic_button = telebot.types.InlineKeyboardButton(text="Политика", callback_data='POLITICS')
queer_v_button = telebot.types.InlineKeyboardButton(text="Сплетни", callback_data='queer_voices')
sport_button = telebot.types.InlineKeyboardButton(text="Спорт", callback_data='sport')
style_beauty_button = telebot.types.InlineKeyboardButton(text="Стиль", callback_data='style_beauty')
the_worldpost_button = telebot.types.InlineKeyboardButton(text="Мировые новости", callback_data='the_worldpost')
travel_button = telebot.types.InlineKeyboardButton(text="Путешествия", callback_data='travel')
weddings_button = telebot.types.InlineKeyboardButton(text="Свадьбы", callback_data='weddings')

keyboard.add(business_button, comedy_button, crime_button, divorce_button,
             food_drink_button, home_living_button, politic_button,
             queer_v_button, sport_button, style_beauty_button, 
             the_worldpost_button, travel_button, weddings_button
            )

@bot.message_handler(commands=['start', 'help'])
def hello_messages(command):
    if command.text == "/start":
        # Что должен сделать бот, если пользователь инициировал взаимодействие
        # Приветствие, объяснение доступных команд и т.д.
        bot.send_message(command.chat.id, # в какой чат отправляем сообщение
                         "Приветствую! Правила следующие: ... \n Какие новости вы хотите почитать?", # сообщение
                         reply_markup=keyboard
                        )
    if command.text == "/help":
        # Отпрваить в ответ справку
        bot.send_message(command.chat.id, # в какой чат отправляем сообщение
                         "Я могу: 1. ... \n 2. ... \n Правила следующие: ..." # сообщение
                        )
        

@bot.message_handler(content_types=["text", "sticker"])
def read_messages(message):
    print(message)
    bot.send_message(message.chat.id, # в какой чат отправляем сообщение
                     "Я могу предложить новости из следующих категорий: ", # сообщение
                     reply_markup=keyboard # добавим клавиатуру в сообщение
                    )


@bot.callback_query_handler(func=lambda call: True)
def get_callback(call):
    # print(call)
    bot.send_message(call.from_user.id, # в какой чат отправляем сообщение
                     "Ищу подходящие новости", # сообщение
                    )

    # 1. Парсим новости за вчера
    yesterday = datetime.now() - timedelta(1) # специальный класс для времени
    yesterday_str = datetime.strftime(yesterday, '%Y-%m-%d')
    news = parse_news(yesterday_str) # передать дату
    # 2. Предобработка
    news = apply_prep(news)
    # 3. Классифицируем новости 
    cats = classify(news)

    texts = get_news_by_cat(news, call.data, cats)

    bot.send_message(call.from_user.id, # в какой чат отправляем сообщение
                     "Вот что я могу сказать об этой теме:", # сообщение
                    )
    for head, short_desc in texts: 
        bot.send_message(call.from_user.id, # в какой чат отправляем сообщение
                        head+ short_desc, # сообщение
                        )
bot.polling()