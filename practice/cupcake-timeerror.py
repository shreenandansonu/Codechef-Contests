from time import time
for _ in range(int(input())):
    st=time()
    max=0
    n=int(input())
    for j in range(1,n+1):
        if(max<=n%j):
            max=n%j
            maxi=j
    print(maxi)
    et=time()
    tt=et-st
    print('total time '+ str(tt))