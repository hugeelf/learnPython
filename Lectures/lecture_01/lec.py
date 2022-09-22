# print ("Hello world")
value = None #пустую переменную нельзя определить, но можно задать None и затем использовать переменную так, как нужно
a = 123
b = 1.23
# print (type(a))
# print (type(b))
# print (type(value))
value = a+b
print (value)
s = 'string' # объявление строки для символов можно использовать esc последовательности

# интерполяция
print (a, '-', b, '-', s)
print ('{} - {} - {}'.format(a,b,s))
print (f'{a} - {b} - {s}')
print ('{2} - {0} - {1}'.format(a,b,s))

# Логическая переменная
f=True
print (f)
print (type(f))

# списки - замена массивам в C#
list = [2,3,4,5,6] # не миксуй данные (выбрал строки, то заполняй один список строками)
print (list)

#ввод и вывод данных
#print () # вывод
#input () # ввод

print ('введите a')
a = int (input())
print ('введите b')
b = int (input())
print (f'{a} + {b} = {a+b}')
print (f'{a} {b}')

a = 1.3
b = 3
c = a*b
d = round(a*b)
e = round(a*b,3)
print (f'{c} без округления {d} с округлением {e} с указанием количества знаков для округления')
a = 5
print (a)
a+=5
print(a)
# f =[1,2,3,4]
# is_odd = f[0]%2==0 равнозначно not f[0]%2 дадут false

a = int(input('a= '))
b = int(input('b= '))
if a > b:
    print (a)
else:
    print (b)

original = 2323475
inverted = 0
while original !=0:
    inverted = inverted*10 + (original%10)
    original//=10
else:
    print ('цикл выполнился, а эта строчка выводится, при условии, что цикл выполнился полностью и пора бы из него выыходить. Это не обязательно использовать')
print (inverted)

print ('for - работает аналогично C#')
for i in 1,2,3,4,5,6:
    print (i**2)

list = [1,2,3,4,5,6,7,8,9,10]
for i in list: # можно разбирать строки
    print (i**2)
 
for i in range(10): # возможно использовать диапазон range(1,5) - получим 1,2,3,4 можно указать шаг или приращение range (1,10,2) - получим 1,3,5,7,9
    print (i)

# имеется встроенная справка по языку help(text.title) - можно использовать для всех подсказок (функций)!!!
text = 'qwerty'
# help(text.title)
# help(str)
# help(list.pop)

# def function_name (x):
#     тело функции

