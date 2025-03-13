import telebot
from bot_logic import detect_trash # Импортируем функции из bot_logic


bot = telebot.TeleBot("7428097385:AAH17N0Vuij__A_aFm9HeugQ3o87aH8kHHA")

@bot.message_handler(commands=['start'])
def send_1(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши /smile чтобы узнать незнаю что ")

@bot.message_handler(commands=['smile'])
def send_2(message):
    bot.reply_to(message, "Пришли фотку и я что-то скажу")


    @bot.message_handler(content_types=["photo"])
    def handle_photo(message):
        file_info = bot.get_file(message.photo[-1].file_id)
        file_name = file_info.file_path.split("/")[-1]
        downloaded_file = bot.download_file(file_info.file_path)
        
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

        result = detect_trash(downloaded_file)
        bot.send_message(message.chat.id, result)
            


# Запускаем бота
bot.polling()
