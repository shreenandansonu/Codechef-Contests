from time import time
for _ in range( int(input())):
    n,d=map(int,input().split(' '))
    a=time()
    total=1
    if d<=10:
        total=(2**(d))
    if 21>=d>10:
        total=1024*(3**(d-10))
    if d>=22:
        total=n
    if total>n:
        print(n)
    else:
        print(total)
    b=time()
    print(b-a)
