for _ in range(int(input())):
    N,X=map(int,input().split(" "))
    if X%2==0:
        if (N-X)%2==0:
            print("YES")
        else:
            print("NO")
    else:
        if (N-X)%2!=0:
            print("YES")
        else:
            print("YES")        
