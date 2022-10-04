# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import my_lib
length_of_sequence = int(input('Введите длину последовательности: '))
sequence = my_lib.almost_random_list(length_of_sequence)
print(sequence)
answer = my_lib.find_no_double(sequence)
print(answer)
