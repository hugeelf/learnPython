from telebot.async_telebot import AsyncTeleBot
import candy_game
TOKEN = ''
bot = AsyncTeleBot(TOKEN)

candy_lib = {}
def to_candy_lib(id, count):
    global candy_lib
    candy_lib[id] = count

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    to_candy_lib(message.from_user.id, 100)
    await bot.reply_to(message, f'У меня есть {candy_lib[message.from_user.id]} конфет. '
                 f'Ты можешь брать от 1 до 28 за ход. Я тоже. '
                 f'Тот, кто заберет последнюю - победил.\n\n'
                 f'Ты начинаешь. \n\n'
                 f'Сколько конфет хочешь забрать?')

@bot.message_handler(func=lambda m: True)
async def echo_all(message):
	global candy_lib
	candy = candy_lib[message.from_user.id]
	try:
		int(message.text)
	except ValueError:
		await bot.reply_to(
			message, 'Чтобы забрать конфеты введи число конфет цифрами. Помни, ты можешь взять от 1 до 28 конфет')
	else:
		if int(message.text) > 28 or int(message.text) < 1 or int(message.text) > candy:
			await bot.reply_to(message, 'Ты не можешь взять столько конфет.')
		else:
			await bot.reply_to(message, 'Отлично')
			candy -= int(message.text)
			candy_lib[message.from_user.id] = candy
			await bot.reply_to(message, f'Осталось {candy} конфет. ')
			if candy == 0:
				await bot.reply_to(
					message, 'Ты победил. Чтобы начать заново напиши /start')
				exit()
			bot_candy = candy_game.gen_bot_candy(candy)
			if bot_candy == 0:
				await bot.reply_to(
					message, 'Я здаюсь, ты победил. Чтобы начать заново напиши /start')
				exit()
			await bot.reply_to(message, f'Я возьму {bot_candy} конфет')
			candy -= int(bot_candy)
			candy_lib[message.from_user.id] = candy
			await bot.reply_to(message, f'Осталось {candy} конфет. ')
			if candy == 0:
				await bot.reply_to(
					message, 'Ты проиграл. Чтобы начать заново напиши /start')


import asyncio
asyncio.run(bot.polling())