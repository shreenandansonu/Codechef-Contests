for _ in range(int(input())):
    N=int(input())
    A=[]
    if N%2==0:
        j,k=0,1
        for i in range(N):
            if i%2==0:
                A.append(N-j)
                j+=1
            else:
                A.append(k)
                k+=1
    else:
        j,k=0,1
        for i in range(1,N+1):
            if i%2==0:
                A.append(k)
                k+=1 
            else:
                A.append(N-j)
                j+=1       
    A.reverse()
    for m in A:
        print(m,end=" ")