for _ in range (int(input())):
    X,Y=map(int,input().split(' '))
    if Y==0:
        print(X)        
    elif X==Y:
        print(X+Y-1)
    else:
        print(X+Y)
        