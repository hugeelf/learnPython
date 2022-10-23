import telebot
import candy_game
TOKEN = ''
bot = telebot.TeleBot(TOKEN)

candy_lib = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global candy_lib
    candy_lib[message.from_user.id] = 100
    bot.reply_to(message, f'У меня есть {candy_lib[message.from_user.id]} конфет. '
                 f'Ты можешь брать от 1 до 28 за ход. Я тоже. '
                 f'Тот, кто заберет последнюю - победил.\n\n'
                 f'Ты начинаешь. \n\n'
                 f'Сколько конфет хочешь забрать?')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	global candy_lib
	candy = candy_lib[message.from_user.id]
	try:
		int(message.text)
	except ValueError:
		bot.reply_to(
			message, 'Чтобы забрать конфеты введи число конфет цифрами. Помни, ты можешь взять от 1 до 28 конфет')
	else:
		if int(message.text) > 28 or int(message.text) < 1 or int(message.text) > candy:
			bot.reply_to(message, 'Ты не можешь взять столько конфет.')
		else:
			bot.reply_to(message, 'Отлично')
			candy -= int(message.text)
			candy_lib[message.from_user.id] = candy
			bot.reply_to(message, f'Осталось {candy} конфет. ')
			if candy == 0:
				bot.reply_to(
					message, 'Ты победил. Чтобы начать заново напиши /start')
				exit()
			bot_candy = candy_game.gen_bot_candy(candy)
			if bot_candy == 0:
				bot.reply_to(
					message, 'Я здаюсь, ты победил. Чтобы начать заново напиши /start')
				exit()
			bot.reply_to(message, f'Я возьму {bot_candy} конфет')
			candy -= int(bot_candy)
			candy_lib[message.from_user.id] = candy
			bot.reply_to(message, f'Осталось {candy} конфет. ')
			if candy == 0:
				bot.reply_to(
					message, 'Ты проиграл. Чтобы начать заново напиши /start')
bot.infinity_polling()
