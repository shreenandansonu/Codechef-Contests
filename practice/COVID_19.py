import math
for _ in range (int(input())):
    N,M=map(int,input().split())
    a=(math.ceil(M/2))*(math.ceil(N/2))
    print(a)