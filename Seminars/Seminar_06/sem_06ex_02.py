# Дана последовательность чисел. Получить список уникальных элементов заданной 
# последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
user_list = [1, 2, 3, 5, 1, 5, 3, 10]
answer = [i for i in user_list if user_list.count(i)==1]
print (answer)