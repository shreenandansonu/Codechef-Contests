for _ in range( int(input())):
    n,d=map(int,input().split(' '))
    total=1
    for i in range(1,d+1):
        if i<=10:
            total=total*2
        elif i>10:
            total=total*3
    if total>n:
        print(n)
    else:
        print(total)