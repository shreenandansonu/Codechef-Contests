for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split(" ")))
    S=A[0]+A[-1]
    for x in range(1,N):
        if A[x-1]+A[(x)]>S:
            S=A[x-1]+A[(x)]
    print(S)