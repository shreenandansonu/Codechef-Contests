n,k=map(int,input().split())
total=0
for i in range(0,n,1):
    x=int(input())
    if (x%k==0):
        total+=1
print(total)
