# 2) Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.


our_list = ['1','2','4fdf', 'hgdkfj', 'hrty']
number = str(input('Введите число для поиска'))
# count = 0
# for i in our_list:
#     if i == number:
#         count=1
#     else:
#         continue
# if count >0:
#     print ('YES')
# else:
#     print ('NO')
if number in our_list:
    print ('YES')
else:
    print('NO')