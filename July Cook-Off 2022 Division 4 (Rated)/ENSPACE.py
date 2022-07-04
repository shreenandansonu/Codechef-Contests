for _ in range(int(input())):
    N,X,Y=map(int,input().split(" "))
    if N>=(X+Y*2):
        print("YES")
    else:
        print("NO")