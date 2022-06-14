def ap_series(A,d,n):
    i=1
    sum=0

    while i<=n:
        a=A+(i-1)*d
        print(a,end=" ")
        i+=1

    print("\n")
    i=1
    while i<=n:
        a=A+(i-1)*d
        a=a*a
        sum+=a
        print(a,end=" ")
        i+=1
    print("\n")
    print(sum)

t=int(input())
j=1
while (j<=t):
    x = list(map(int, input().split()))
    A=x[0]
    d=x[1]
    n=x[2]
    ap_series(A,d,n)
    j+=1