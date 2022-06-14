import math as m
t=int(input())
for i in range(0,t,1):
    n=int(input())
    f=1
    for j in range(1,n+1,1):
        f=f*j
    print(f)