for _ in range(int(input())):
    A,B,C,P,Q,R=map(int,input().split(' '))
    rsum=A+B+C
    tsum=P+Q+R
    winingnum=tsum//2
    if winingnum>rsum:
        if winingnum<rsum-A+P or winingnum<rsum-B+Q or winingnum<rsum-C+R:
            print('YES')
        else:
            print('NO') 
    else:
        print('YES')