# Задачи для семинара:
# 1)Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
our_list = [1,2,3,4,4,5,5,6]
for i in our_list:
    count = 0
    for x in our_list:
        if x == i:
            count+=1
        else:
            continue
    if count == 1:
        print(i)