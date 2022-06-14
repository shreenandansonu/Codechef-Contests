import math


for _ in range(int(input())):
    N=int(input())
    x=0
    while N>0:
        if N>100:
            y=math.floor(N/100)
            x=x+y
            N=N-100*y
        elif 100>N>=50:
            y=math.floor(N/50)
            x=x+y
            N=N-50*y
        elif 50>N>=10:
            y=math.floor(N/10)
            x=x+y
            N=N-10*y
        elif 10>N>=5:
            y=math.floor(N/5)
            x=x+y
            N=N-5*y
        elif 5>N>=2:
            y=math.floor(N/2)
            x=x+y
            N=N-2*y
        elif 2>N>=1:
            y=math.floor(N/1)
            x=x+y
            N=N-1*y
    print(x)