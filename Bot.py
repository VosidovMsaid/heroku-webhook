import telebot

bot = telebot.TeleBot("2019591321:AAEKiWhzkPFqhJc6q9kPJHQw8Nkk64BXd44")

@bot.message_handler(content_types=['text'])
def send_echo(message):
     bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
