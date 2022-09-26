# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

number = float(input(
    'Введите вещественное число (помни - отдели целую часть от дробной точкой, не запятой): '))
is_it_sub_zero = 1
if number <0:
    number=-number
    is_it_sub_zero=-1

temp_string = str(number).replace('.', '')
answer = 0
for i in temp_string:
    answer += int(i)
print(answer*is_it_sub_zero)
