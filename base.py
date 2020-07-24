import telebot
from substructure import MessageResponse

##############

token = open('token.txt').read()
bot = telebot.TeleBot(token)

##############

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    msg = MessageResponse(message)
    msg.AddResponse()
    bot.send_message(msg.author, msg.response)

bot.polling(none_stop = True, interval = 0)