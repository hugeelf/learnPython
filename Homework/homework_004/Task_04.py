# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
import my_lib


k = int(input('Введите k: '))
answer = my_lib.formula_output(k)
# print(answer)
with open('file2.txt', 'w') as data:
    data.write(answer)
