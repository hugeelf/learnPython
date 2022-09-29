# 4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
number = int(input('Введите N: '))
elements = [i for i in range(-number, number+1)]
positions = list(map(int, input(
    'введите позиции для поиска произведения через пробел: ').split()))
composition = 1
for i in positions:
    composition *= elements[i-1]
print(
    f'Произведение элементов списка {elements}, находящихся на позициях {positions} = {composition}')
