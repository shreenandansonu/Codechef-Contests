def sum(m,k):
    summation=0
    for x in range(1,k+1):
        summation+=m[-x]
    return summation

for _  in range(int(input())):
    N,k=map(int,input().split(' '))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort(),B.sort()
    a=[]
    [a.append(x) for x in A if x not in a]
    b=[]
    [b.append(Y) for Y in B if Y not in b]
    lowsum=[sum(a,k),sum(b,k)]
    lowsum.sort()
    print(lowsum[0])
