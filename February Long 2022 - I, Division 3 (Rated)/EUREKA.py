import math
for _ in range(int(input())):
    N=int(input())
    M=(0.143*N)**N
    X=math.floor(M)
    if M-X<0.5:
        print(X)
    else:
        print(X+1)