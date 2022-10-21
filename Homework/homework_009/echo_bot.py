import telebot
import candy_game

API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)

# candy = 100


@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.reply_to(message, 'Сыграем в игру')
    bot.reply_to(message, f'У меня есть 100 конфет. '
                          f'Ты можешь брать от 1 до 28 за ход. Я тоже. '
                          f'Тот, кто заберет последнюю - победил.\n\n'
                          f'Ты начинаешь. \n\n'
                          f'Сколько конфет хочешь забрать?')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    candy = 100
    if candy == 0:
        candy = 100
    elif int(message.text) > 28 or int(message.text) < 1 or int(message.text) > candy:
        bot.reply_to(message, 'Ты не можешь взять столько конфет.')
    else:
        bot.reply_to(message, 'Отлично')
        candy -= int(message.text)
        bot.reply_to(message, f'Осталось {candy} конфет. ')
        if candy == 0:
            bot.reply_to(message, f'Осталось {candy} конфет. ')
            bot.reply_to(message, 'Ты победил, давай начнем с начала\n Сколько конфет хочешь забрать?')
            candy = 100
        bot_candy = candy_game.gen_bot_candy(candy)
        if bot_candy ==0:
            bot.reply_to(message, 'Я здаюсь, ты победил. давай начнем с начала\n Сколько конфет хочешь забрать?')
            candy = 100
        bot.reply_to(message, f'Я возьму {bot_candy} конфет')
        candy -= bot_candy
        if candy == 0:
            # bot.reply_to(message, f'Осталось {candy} конфет. ')
            bot.reply_to(message, 'Я победил, давай начнем с начала\n Сколько конфет хочешь забрать?')
            candy = 100
        bot.reply_to(message, f'Осталось {candy} конфет. ')


bot.polling()

# pip3 uninstall telebot
# pip3 uninstall PyTelegramBotAPI
# pip3 install pyTelegramBotAPI
# pip3 install --upgrade pyTelegramBotAPI
