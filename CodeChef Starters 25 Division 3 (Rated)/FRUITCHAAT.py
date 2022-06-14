import math
for _ in range(int(input())):
    X,Y=map(int,input().split(' '))
    if X/2>Y:
        print(Y)
    else:
        print(math.floor(X/2))
