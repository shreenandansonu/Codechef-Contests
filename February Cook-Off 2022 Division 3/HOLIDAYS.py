for _ in range(int(input())):
    N,W=map(int,input().split(' '))
    A=input().split(' ')
    A.sort(reverse=True)
    ET=0
    for x in A:
        if ET>=W:
            ET+=int(x)
            N-=1
        else:
            print(N)
            break
    if ET==W and N==0:
        print(0)