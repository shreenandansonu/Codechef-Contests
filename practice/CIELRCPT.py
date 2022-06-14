import math
for _ in range(int(input())):
    p=int(input())
    i=0
    while p>0:
        n=math.floor(math.log(p,2))
        if n<=11:
            p=p-2**n
            i+=1
        else:
            p=p-2**11
            i+=1
    print(i)