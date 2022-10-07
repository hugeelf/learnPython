# Напишите программу для игры в крестики-нолики
import tik_tak_toe

game_continue = True
game_map = ['1','2','3','4','5','6','7','8','9']
# game_map = ['X','2','X','4','O','X','O','X','O']
player = 'X'
bot = 'O'
wining_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
game_mooves = []
counter = 0

tik_tak_toe.print_map(game_map)
while game_continue==True:
    print('Ход игрока\n')
    pos = tik_tak_toe.player_input_check()
    pos = tik_tak_toe.check_moves(pos, game_mooves)
    game_map.insert(pos-1,player)
    game_map.pop(pos)
    tik_tak_toe.print_map(game_map)
    tik_tak_toe.win_check(game_map,wining_combinations,counter)
    counter+=1
    print('\n Ходит бот ')
    pos = tik_tak_toe.bot_move(game_map,player,bot)
    game_map.insert(pos-1,bot)
    game_map.pop(pos)
    tik_tak_toe.print_map(game_map)
    counter+=1
    tik_tak_toe.win_check(game_map,wining_combinations, counter)
    pos = tik_tak_toe.check_moves(pos, game_mooves)
    