# Цифровой корень — это рекурсивная сумма 
# всех цифр числа.
# Учитывая n, возьмите сумму цифр n. 
# Если это значение имеет более одной цифры, 
# продолжайте уменьшать таким образом, 
# пока не будет получено однозначное число. 
# Ввод будет неотрицательным целым числом.
# Примеры
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
# Нумерология))



def digit_root (number):
    answer = 0
    if number<10:
        return number
    else:
        return digit_root(to_digit(number))      

def to_digit (number):
    answer = 0
    while number%10 !=0:
        answer += number%10
        number = number //10
    return answer

number = int(input('Введите число'))
answer = digit_root(number)
# answer = to_digit(number)
print(answer)