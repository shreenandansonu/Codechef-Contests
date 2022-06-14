for _ in range(int(input())):
    q,p=map(int,input().split())
    if q<1000:
        print(format(p*q,".6f"))
    else:
        x=((p*q)-((p*q)/10))
        print(format(x,".6f"))