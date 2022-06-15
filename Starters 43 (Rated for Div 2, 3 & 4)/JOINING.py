import math
from re import X
from tkinter import Y


for _ in range(int(input())):
    N,K=map(int,input().split(" "))
    X=int(math.ceil(N/5))
    Y=int(math.ceil(K/5))
    if X>Y:
        print(X-Y)
    else:
        print(0)