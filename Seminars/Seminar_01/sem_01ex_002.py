# a = [int(input()), int(input())]
# if a[0]//a[1]==a[1] or a[1]//a[0]==a[0]:
#     print ('одно число является квадратом другого')
# else:
#     print('no')


a = list(map(int, input().split()))
if a[0]//a[1]==a[1] or a[1]//a[0]==a[0]:
    print ('одно число является квадратом другого')
else:
    print('no')