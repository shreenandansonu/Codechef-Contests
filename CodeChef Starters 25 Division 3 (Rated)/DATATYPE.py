for _ in range(int(input())):
    N,X=map(int,input().split(' '))
    if X>N:
        while X>N:
            X=X-1-N
        print(X)
    else:
        print(X)