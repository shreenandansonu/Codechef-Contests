for _ in range (int(input())):
    Z,Y,A,B,C=map(int,input().split(' '))
    if (Z-(A+B+C+Y))>=0:
        print('YES')
    else:
        print('NO')