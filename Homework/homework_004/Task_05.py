# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 2*x² + 4*x + 5 3*x² +10*x + 6
# Вывод:
# 5*x² + 14*x + 11
import sympy
with open('multimem_one', 'r') as first_expression:
    a = first_expression.read()
with open('multimem_two', 'r') as second_expression:
    b = second_expression.read()
result = sympy.simplify(f'{a} + {b}')
with open('multi_answer', 'w') as answer:
    answer.write(str(result))
