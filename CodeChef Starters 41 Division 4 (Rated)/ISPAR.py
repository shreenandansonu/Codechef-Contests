for _ in range (int(input())):
    N,K=map(int,input().split(" "))
    if K>2:
        print("EVEN")
    elif K==2:
        print("ODD")
    else:
        if N%2==0:
            print("EVEN")
        else:
            print("ODD")    