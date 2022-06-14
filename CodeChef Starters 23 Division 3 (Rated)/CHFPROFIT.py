for _ in range(int(input())):
    x,y,z=map(int,input().split(' '))
    profit=(x*z)-(x*y)
    print(profit)