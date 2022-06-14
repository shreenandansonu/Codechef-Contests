facto_of=[]
length=0
for _ in range(int(input())):
    N=int(input())
    for k in range(2,N+1):
        if N%k==0 and k!=1:
            m=int(N/k)
            for M in range(1,m+1):
                if m%M==0:
                    facto_of.append(M)
            if length<len(facto_of):
                length=len(facto_of)
                facto_of.clear()
                smallfactor=k
    print(smallfactor)