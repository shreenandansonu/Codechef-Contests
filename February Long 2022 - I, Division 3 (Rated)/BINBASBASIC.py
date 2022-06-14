import math
for _ in range(int(input())):
    N,K=map(int,input().split(' '))
    S=input()
    if K==0:
        print('NO')
    elif N>K and  K!=0 and (1<=N<=1000):
        i=0
        for x in range(0,math.floor(N/2)):
            if S[x]!=S[-1-x]:
                i+=1
        if i==K :
            print('YES')
        else:
            print('NO')    
    else:
        print('NO')        