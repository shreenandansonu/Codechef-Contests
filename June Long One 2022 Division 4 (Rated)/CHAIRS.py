for _ in range (int(input())):
    X,Y=map(int,input().split(" "))
    if X>Y:
        print(X-Y)
    else:
        print(0)