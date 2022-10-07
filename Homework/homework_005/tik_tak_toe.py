import random
def player_input_check():
    check = False
    while check == False:
        input_check = input('Введите номер клетки, в которую хотите поставить Х: ')
        try:
            int(input_check)
            if int(input_check)>9 or int(input_check)<1:
                print('Введите цифру от 1 до 9')
            else:
                check = True
        except:
           print('Введите цифру от 1 до 9') 
        
    return int(input_check)

def print_map (game_map):
    for i in range(0,9,3):
        print(game_map[i],game_map[i+1],game_map[i+2])

def check_moves(player_moove, game_mooves):
    check = False
    while check == False:
        if player_moove in game_mooves:
            print('Эта клетка уже занята')
            player_moove = player_input_check()
        else:
            game_mooves.append(player_moove)
            check=True
    return player_moove

def win_check(game_map,wining_combinations, counter):
    for i in wining_combinations:
        if game_map[i[0]]==game_map[i[1]]==game_map[i[2]] == 'X':
            print(f'Победил игрок играющий Крестиками (Х)')
            exit()
        elif game_map[i[0]]==game_map[i[1]]==game_map[i[2]] == 'O':
            print(f'Победил игрок играющий Ноликами (O)')
            exit()
        elif counter == 9:
            print('Ничья')
            exit()

def bot_move(game_map,player,bot):
    bot_move_check = False
    while bot_move_check == False:
        pos = random.randint(1,9)
        if game_map[pos-1]==player or game_map[pos-1]==bot:
            continue
        else:
            bot_move_check = True
    return pos
