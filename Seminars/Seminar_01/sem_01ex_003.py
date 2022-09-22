# # напишите программу, которая принимает на вход n чисел и выводит максимум из них.
# a = input().split()
# i=1
# max = int(a[0])
# while i < len(a):
#     if max < int(a[i]):
#         max = int(a[i])
#         i+=1
#     else:
#         i+=1
# print (max)
    
# a = list(map(int, input().split()))
# maximum = max(a)
# print (maximum)

print (max(list(map(int, input().split()))))