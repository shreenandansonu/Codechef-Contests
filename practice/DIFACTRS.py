N=int(input())
factors=[]
for _ in range(1,N+1):
    if N%_==0:
        factors.append(_)
factors.sort()
print(len(factors))
for __ in (factors):
    print(__, end=" ")