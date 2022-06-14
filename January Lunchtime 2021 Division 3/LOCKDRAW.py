for _ in range(int(input())):
    A,B,C=map(int,input().split(' '))
    lst=[A,B,C]
    lst.sort()
    if (lst[0]+lst[1]==lst[2]):
        print('YES')
    else:
        print('NO')