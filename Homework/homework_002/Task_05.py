# Реализуйте алгоритм перемешивания списка.
import random
from random import randint
first_list = [randint(0,9999) for i in range(randint(2,12))]
print(first_list)
random.shuffle(first_list)
print(first_list)