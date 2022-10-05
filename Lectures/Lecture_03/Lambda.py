# # # # def sum(x, y):
# # # #     return x+y


# # # # def sum(x, y): return x+y


# # # def mult(x, y):
# # #     return x*y


# # # def calc(op, a, b):
# # #     print(op(a, b))
# # #     return op(a, b)


# # # calc(lambda x,y: x+y, 10, 12)


# # # list comprehension
# # # [exp for item in iterable]
# # # [exp for item in iterable if condition]
# # def f(x):
# #     return x**3
# # a = [i for i in range (1, 10)if i%2==0]
# # print (a)
# # print (type(a))

# # b = [(i, i) for i in range (1, 10)if i%2==0]
# # print (b)
# # print (type(b))

# # c = [(i, f(i)) for i in range (1, 10)if i%2==0]
# # print (c)
# # print (type(c))
# with open ('file', 'r') as file:
#     data = file.read().split()
# print (data)

# def select(f,col):
#     return [f(x) for x in col]

# def where (f,col):
#     return [x for x in col if (f(x))]

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select (lambda x: (x,x**2), res)
# print (res)
#

# map
# li = [x for x in range(1,20)]
# li = list(map(lambda x: x+10, li))
# print (li)

# data = list(map(int,input().split()))
# print (data)
with open('file', 'r') as file:
    data = file.read().split()


res = list(map(int, data))
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)


user = ['user1','user2','user3','user4']
id = [4,5,6,7]
salary = [900,800,700]
data = list(zip (user, id))
print (data)
salary = list(enumerate(salary))
print (salary)