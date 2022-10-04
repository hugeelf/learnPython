import random
from random import randint


def slicer(string):
    return string[int(string.find('.'))+1::]

# находит все делители числа нам это не подходит.
# Все хорошо работает при числах до нескольки тысяч. для числа 10000 я так и не дождался вывода.


def find_divider(number):
    answer = [1, ]
    for i in range(2, number):
        if number % i == 0:
            answer.append(i)
            for j in range(2, number):
                if number % i**j == 0:
                    answer.append(i**j)
    return list(set(answer))

#  А это уже то, что нужно - находит простые множители числа


def find_simple_divider(n):
    i = 2
    answer = []
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n //= i
            i = 2
        else:
            i += 1
    answer.sort()
    return answer


def almost_random_list(n):
    return [randint(0, 10) for i in range(randint(n, n))]


def find_no_double(a):
    result = []
    for i in a:
        if a.count(i) == 1:
            result.append(i)
    return result


def formula_output(k):
    answer = ''
    for i in range(0, k+1):
        cf = random.randint(0, 101)
        if cf == 0:
            continue
        elif k-i == 0:
            answer += f'{cf} '
        else:
            answer += f'{cf}*X^{k-i} + '
    last_answer = answer
    if answer[-2] == '+':
        last_answer = answer[0:len(answer)-2]

    last_answer += '= 0'
    return last_answer
