import random
from random import randint


def player_moove(candy):
    while candy != 0:
        lot = randint(0, 1)
        winner = 'Игрок'
        if lot == 1:
            print('Начинает бот')
            bot_candy = randint(1,28)
            print(f'Я возьму {bot_candy}\n')
            candy-=bot_candy
            print(f'Осталось {candy} конфет\n')
            lot =0
        else:
            print('Сколько конфет вы хотите взять?\n')
            player_candy = int(input())
            if player_candy > 28 or player_candy < 1 or player_candy > candy:
                print(
                    'Вы не можете взять столько конфет. Попробуйте еще раз\n')
            else:
                candy -= player_candy
                print(f'Осталось {candy} конфет\n')
                bot_candy = randint(1, 28)
                if candy <= 28 and candy>0:
                    bot_candy = candy
                    winner = 'Бот. В следующий раз повезет'
                elif candy<=56 and candy>28:
                    bot_candy = candy-29
                    if bot_candy == 0:
                        print(f'Я сдаюсь. Ты победил')
                        exit()
                elif candy ==0:
                    print(f'Игра закончена. Победитель {winner}.')
                    exit()
                print(f'А я возьму {bot_candy}')
                candy -= bot_candy
                print(f'Осталось {candy} конфет\n')
    print(f'Игра закончена. Победитель {winner}.')
    exit()
