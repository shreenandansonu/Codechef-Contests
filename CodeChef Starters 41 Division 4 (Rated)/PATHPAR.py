for _ in range (int(input())):
    N,K=map(int,input().split(" "))
    if N%2==0:
        print("YES")
    else:
        if K==1:
            print("YES")
        else:
            print("NO")