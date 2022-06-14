for _ in range(int(input())):
    N=int(input())
    A=str(input())
    B=str(input())
    C=[]
    i=0
    for j in range(N):
        if A[j]!=B[j]:
            if B[j] not in C:
                C.append(B[j])
                i+=1
    print(i)
