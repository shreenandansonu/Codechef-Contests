for _ in range (int(input())):
    a,b=map(int,input().split())
    s=[a,b]
    s.sort()
    print(s[-1],end=" ")
    print(int(a+b))
