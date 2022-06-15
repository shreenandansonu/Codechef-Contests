import math


for _ in range(int(input())):
    N,X=map(int,input().split(" "))
    if N<52:
        if int(math.ceil(N/2))==X:
            pal="a"
            i=1
            while i<X:
                pal+=chr(97+i)
                i+=1
            if N%2!=0:
                j=X-2
                while j>=0:
                    pal+=chr(97+j)
                    j-=1
            else:
                k=X-1
                while k>=0:
                    pal+=chr(97+k)
                    k-=1
            print(pal)

                
        else:
            print(-1)
    else:
        print(-1)