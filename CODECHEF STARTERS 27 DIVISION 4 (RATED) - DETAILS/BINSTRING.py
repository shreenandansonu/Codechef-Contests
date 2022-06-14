for _ in range(int(input())):
    N=int(input())
    S=input()
    lst=[]
    print(S)
    for x in (0,N):
        a=list(S)
        a.pop(x)
        print(a)
        print(S)
        lst.append(a)
    lst=set(lst)
    print(len(lst))
