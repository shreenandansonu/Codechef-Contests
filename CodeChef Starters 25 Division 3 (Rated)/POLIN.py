for _ in range(int(input())):
    N=int(input())
    X=[]
    Y=[]
    for i in range(1,N+1):
        d=input().split(' ')
        X.append(d[0])
        Y.append(d[1])
    x=set(X)
    y=set(Y)
    lines=N*2-((N-len(x))+(N-len(y)))
    print(lines)
#second attempt
'''
for _ in range(int(input())):
    N=int(input())
    X=[]
    Y=[]
    lines=2*N
    for i in range(N):
        x,y=map(int,input().split(' '))
        if x in X:
            lines-=1
        else:
            X.append(x)
        if y in Y:
            lines-=1
        else:
            Y.append(y)
    print(lines)'''
#first attempt
'''
for _ in range(int(input())):
    N=int(input())
    X=[]
    Y=[]
    for i in range(1,N+1):
        d=input().split(' ')
        X.append(d[0])
        Y.append(d[1])
    x=set(X)
    y=set(Y)
    I,J=0,0
    for i in x:
        a=X.count(i)
        if a>1:
            I+=int(a-1)
    for j in y:
        b=Y.count(j)
        if b>1:
            J+=int(b-1)
    line=int(2*N)-(I+J)
    print(line) '''