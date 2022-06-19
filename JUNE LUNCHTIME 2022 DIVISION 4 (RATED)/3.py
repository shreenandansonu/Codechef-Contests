import math


for _ in range(int(input())):
    X,Y=map(int,input().split(" "))
    print(abs(math.ceil(X/10)-math.ceil(Y/10)))