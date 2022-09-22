#  Напишите программу, которая принимает на вход число N и выводит числа от -N до N
# n = int(input())
# a = n-n*2
# while a<=n:
#     print (a)
#     a+=1

n = int(input())
mass = []
for i in range(-n,n+1,1):
    mass.append(i)
print (mass)