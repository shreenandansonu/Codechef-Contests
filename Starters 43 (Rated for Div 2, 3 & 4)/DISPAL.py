import math
for _ in range(int(input())):
    N,X=map(int,input().split(" "))
    if N>=(2*X)-1:
        if N%2==0:
            pal="a"
            i=1
            while i<X:
                pal+=chr(97+i)
                i+=1
            pal+=(N-2*X)*chr(97)
            k=X-1
            while k>=0:
                pal+=chr(97+k)
                k-=1
            print(pal)
        else:
            if N==(2*X)-1:
                pal="a"
                j=1
                while j<X:
                    pal+=chr(97+j)
                    j+=1
                l=X-2
                while l>=0:
                    pal+=chr(97+l)
                    l-=1
                print(pal)
            else:
                pal="a"
                i=1
                while i<X:
                    pal+=chr(97+i)
                    i+=1
                pal+=(N-2*X)*chr(97)
                k=X-1
                while k>=0:
                    pal+=chr(97+k)
                    k-=1
                print(pal)
    else:
        print(-1)
