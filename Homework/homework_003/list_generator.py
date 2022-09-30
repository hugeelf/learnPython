# заполнение списка последовательностью от start_number до end_number
def list_generator(start_number, end_number):
    generated_list = [i for i in range(start_number, end_number+1)]
    return generated_list

# сумма элементов списка на нечетных позициях


def summator(array):
    sum = 0
    for i in range(1, len(array), 2):
        sum += array[i]
    return sum


# произведение элементов списка первый * последний, второй * предпоследний...
def multiply_of_odd(array):
    new_list = []
    count = -1
    
    for i in range(len(array)//2):
        new_list.append(array[i]*array[count])
        count -= 1
    if len(array) % 2 != 0:
        new_list.append((array[len(new_list)])**2)
    return new_list
