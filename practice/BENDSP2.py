for _ in range (int(input())):
    a,b,c,d=map(int,input().split(' '))
    if (a==b and c==d ) or (a==d and b==c) or (a==c and b==d):
        print('YES')
    else:
        print('NO')