for _ in range(int(input())):
    N =int(input())
    S=input().split(' ')
    S.sort()
    s=set(S)
    MEX=0
    for i in s:
        if i < MEX and S.count(i)>2:

            
