for _ in range (int(input())):
    N,X=map(int,input().split(" "))
    if N%6==0:
        print(int((N/6)*X))
    else:
        print(int(((N//6)*X)+X))
