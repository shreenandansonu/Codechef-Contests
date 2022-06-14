wow=[]
lst1=[]
lemth=[]
for _ in range(int(input())):
    N=int(input())
    for n in range(2,N):
        if N%n==0:
            wow.append(n)
    for k in wow:
        for M in range(1,k):
            if k%M==0:
                lst1.append(M)
        length=len(lst1)
        lst1.clear()
        lemth.append(length)
    max=0
    for y in lemth:
        if max<y:
            max=y
        got=lemth.index(max)
        K=N/wow[got]
        lemth.clear()
        wow.clear()
        print(k)



