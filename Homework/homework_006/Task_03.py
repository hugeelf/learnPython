# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
a = int(input())
b = int(input())
square = lambda a: a*a
if square(a) ==b or square (b) == a:
    print('Yes')
else:
    print('No')

# lambda не уверен, правильно ли я ее использую. Как я понял, lambda нам нужна, чтобы в функции не писать return и сократить код.