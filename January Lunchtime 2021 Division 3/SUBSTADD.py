for _ in range (int(input())):
    N,X,Y=map(int,input().split(' '))
    A=list(map(int,input().split(' ')))
    B=list(map(int,input().split(' ')))
    c=0
    for  x in range (0,N):
        if (B[x]==(A[x]+X)):
            c=c+1
        elif (B[x]==(A[x]+Y)):
            c=c+1
    if c==N:
        print('YES')
    else:
        print('NO')