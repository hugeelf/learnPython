#  Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python(sympy)

import sympy
from sympy.solvers import solve
from sympy import Symbol


def discriminnt(a, b, c):
    return (b**2 - 4*a*c)


def solution(a, b, c):
    if d < 0:
        print('Вещественных корней нет')
    elif d == 0:
        print(f'X = {-(b/2*a)}')
    else:
        print(f'X1 = {(-b-d**0.5)/2*a}, X2 = {(-b+d**0.5)/2*a}')


a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

d = discriminnt(a, b, c)
solution(a, b, c)

x = Symbol('x')
print(solve(a*x**2+b*x+c, x))
