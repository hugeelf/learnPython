# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 12345 - 1235 - пропущено 4

with open ('file', 'r') as file:
    a = list(map(int, file.read().split()))

def find_number(a):
    number = 0
    for i in range (1, len(a)):
        if a[i]-1 != a[i-1]:
            number = a[i]-1
    return number

b = find_number(a)
print (a)
print (b)