def write_data(a):
    with open ('base.txt', 'a', encoding='utf-8') as base:
        base.write(f'{a}\n')

