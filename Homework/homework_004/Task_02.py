# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import my_lib
n = int(input('Введите N: '))
print(f'Простые множители числа {n}: {my_lib.find_simple_divider(n)}')
