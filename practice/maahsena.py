j=0
k=0
n=int(input())
a=list(map(int,input().split()))
for i in range (n):
    if (a[i]%2==0):
        j+=1
    else:
        k+=1
if j>k :
    print("READY FOR BATTLE")
else:
    print("NOT READY")