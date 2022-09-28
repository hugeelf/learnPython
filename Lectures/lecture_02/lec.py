# запись в файл
from pickle import FALSE
import hello as h
import hello
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')  # a - дописать, w - перезаписать все данные
data.writelines(colors)
data.write('\nLine 2 \n')
data.write('Line 3 \n')
data.close()

with open('file2.txt', 'w') as data:
    data.write('line 1 \n')
    data.write('line 2 \n')
# close () не нужно вызывать, так как такая запись автоматически разрывает связь с файлом по окончанию работы с ним.

# чтение из файла
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close

# вызов функции из файла
print(hello.f(1))

print(h.f(1))
# кортежи как неизменяемы список - добавить значение по типу a[0] = 4 не выйдет.
a = (3, 4, 5, 6, 7, 8, 9, 0)
print(a)
print(a[1])
print(a[-1])
for number in a:
    print (number+1)
