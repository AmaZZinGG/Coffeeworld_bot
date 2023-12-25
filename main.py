import telebot
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot('6181869879:AAH7QI8xddZgjlU7arEKuaE-No7O9a0EtAY')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Rooma = types.KeyboardButton("Rooma")
    Dr_Coffee = types.KeyboardButton("Dr_Coffee")
    markup.add(Rooma)
    markup.add(Dr_Coffee)
    bot.send_message(m.chat.id, "Здравствуйте, это бот компании Кофейный мир")
    bot.send_message(m.chat.id, "Выберите марку кофемашины с которой возникла проблема", reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):



    # Если юзер прислал Rooma (1 путь)
    if message.text.strip() == "Rooma":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rom_9 = types.KeyboardButton("A9/A9S")
        rom_10 = types.KeyboardButton("A10/A10S")
        markup.add(rom_9, rom_10)
        answer = bot.send_message(message.chat.id, "Выберите модель кофемашины Rooma", reply_markup=markup)

    # Возвращение в меню
    elif message.text.strip() == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Rooma")
        button2 = types.KeyboardButton("Dr_Coffee")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    # Если юзер прислал Rooma и выбрал A9/A9S (1 путь 1 вариант)
    elif message.text.strip() == "A9/A9S":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a9_turn_and_set = types.KeyboardButton("Включение и настройка напитков A9") #Включение и настройка напитков
        a9_cappuch_set = types.KeyboardButton("Уход за каппучинатором A9") #Уход, чистка и решение проблем каппучинатора
        a9_brew_set = types.KeyboardButton("Уход за заварным устройством A9") #Уход, чистка и решение проблем заварного устройства
        a9_foam_failure = types.KeyboardButton("Отстуствие пены A9") #Отстуствие пены
        a9_clean_cappuch = types.KeyboardButton("Промывка каппучинатора A9") # Промывка каппучинатора
        back_to_menu = types.KeyboardButton("Вернуться в главное меню") # Возвращение в главное меню
        markup.add(a9_turn_and_set, a9_cappuch_set, a9_brew_set, a9_foam_failure, a9_clean_cappuch,back_to_menu)
        answer = bot.send_message(message.chat.id, "Выберите текущий вопрос или проблему", reply_markup=markup)

    elif message.text.strip() == "Включение и настройка напитков A9":
        answer = bot.send_message(message.chat.id, "https://youtu.be/ugBfnN3qlY8")
        answer3 = bot.send_message(message.chat.id, text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Уход за каппучинатором A9":
        answer = bot.send_message(message.chat.id, "https://youtu.be/YVcUKyWXPZw")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Уход за заварным устройством A9":
        answer = bot.send_message(message.chat.id, "https://youtu.be/hfkdb_5MuZQ")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Отстуствие пены A9":
        answer = bot.send_message(message.chat.id, "https://youtu.be/u01eGaBHOl4")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Промывка каппучинатора A9":
        answer = bot.send_message(message.chat.id, "https://youtu.be/HaH9loqUc4E")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    # Если юзер прислал Rooma и выбрал A9/A9S (1 путь 2 вариант)
    elif message.text.strip() == "A10/A10S":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a10_turn_and_set = types.KeyboardButton("Включение и настройка напитков A10") # Включение и настройка напитков А10
        a10_cappuch_set = types.KeyboardButton("Уход за каппучинатором А10") #Уход, чистка и решение проблем каппучинатора А10
        a10_brew_set = types.KeyboardButton("Уход за заварным устройством А10") #Уход, чистка и решение проблем заварного устройства А10
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")  # Возвращение в главное меню
        markup.add(a10_turn_and_set, a10_cappuch_set, a10_brew_set,back_to_menu)
        answer = bot.send_message(message.chat.id, "Выберите текущий вопрос или проблему", reply_markup=markup)

    elif message.text.strip() == "Включение и настройка напитков A10":
        answer = bot.send_message(message.chat.id, "https://youtu.be/9sCofqgCONk")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Уход за каппучинатором А10":
        answer = bot.send_message(message.chat.id, "https://youtu.be/EU0MbNGGwK4")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Уход за заварным устройством А10":
        answer = bot.send_message(message.chat.id, "https://youtu.be/d1fnAajne-s")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    # Если юзер прислал Dr_Coffee
    elif message.text.strip() == "Dr_Coffee":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        F_1011 = types.KeyboardButton("F10/F11")
        markup.add(F_1011)
        answer = bot.send_message(message.chat.id, "Выберите модель кофемашины Dr_Coffee", reply_markup=markup)


    # Если юзер прислал Dr_Coffee и выбрал F10/F11
    elif message.text.strip() == "F10/F11":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        f1011_solve_poss_probl = types.KeyboardButton("Решение возможных проблем")  # Решение возможных проблем F10/F11
        f10011_set_drinks = types.KeyboardButton("Настройка напитков")  # Настройка напитков F10/F11
        f1011_set_cappuch = types.KeyboardButton("Настройка каппучинатора")  # Настройка каппучинатора F10/F11
        f1011_advice_right_use = types.KeyboardButton("Правильное использование")  # Правильное использование F10/F11
        f1011_care_and_clean = types.KeyboardButton("Уход и чистка")  # Уход и чистка F10/F11
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")  # Возвращение в главное меню
        markup.add(f1011_solve_poss_probl, f10011_set_drinks, f1011_set_cappuch, f1011_advice_right_use, f1011_care_and_clean, back_to_menu)
        answer = bot.send_message(message.chat.id, "Выберите текущий вопрос или проблему", reply_markup=markup)
        answer2 = bot.send_message(message.chat.id, "Уважаемый клиент , ознакомьтесь со всеми видеоинструкциями")


    elif message.text.strip() == "Решение возможных проблем":
        answer = bot.send_message(message.chat.id, "https://youtu.be/3nc5LXw2r7E")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Настройка напитков":
        answer = bot.send_message(message.chat.id, "https://youtu.be/4YQbfBM2uP4")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Настройка каппучинатора":
        answer = bot.send_message(message.chat.id, "https://youtu.be/Fx4uFLgWX_0")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Правильное использование":
        answer = bot.send_message(message.chat.id, "https://youtu.be/eX8dphkJkmQ")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")

    elif message.text.strip() == "Уход и чистка":
        answer = bot.send_message(message.chat.id, "https://youtu.be/etvq7rh_eTU")
        answer3 = bot.send_message(message.chat.id,text="Если видеоиснтрукции не помогли решить проблему, то присылайте видео с описанием вашей проблемы в WhatsApp по номеру +7 926 607 83 37 (ПН-ПТ, 9:00-18:00)")
# Запускаем бота
bot.polling(none_stop=True, interval=0)
   