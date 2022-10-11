# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите N: '))
multiply = lambda a,b: a*b
answer =[]
a = 1
for i in range(1, n+1):  
    a = multiply(a,i)
    answer.append(a)
print(answer)
# lambda не уверен, правильно ли я ее использую. Как я понял, lambda нам нужна, чтобы в функции не писать return и сократить код.