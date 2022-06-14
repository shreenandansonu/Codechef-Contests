for _ in range (int(input())):
    N=int(input())
    A=list(map(int,input().split(" ")))
    ONE=A.count(1)
    MONE=A.count(-1)
    x=abs(ONE-MONE)
    if x%2==0:
        print(int(x/2))
    else:
        print(-1)