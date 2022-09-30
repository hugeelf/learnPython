# '1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# our_list = [i for i in range(1, 5)]
# print(our_list)
# sum = 0
# for i in range(1, len(our_list), 2):
#     sum += our_list[i]
# print(sum)

import list_generator as g
our_list = g.list_generator(int(input('Введите начальное число для элементов: ')), int(
    input('Введите конечное число для элементов: ')))
print(our_list)
print(g.summator(our_list))
