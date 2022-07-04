import math


for _ in range(int(input())):
    X,Y,Z=map(int,input().split(" "))
    print(int(math.ceil(X/Y)*Z))