r=int(input())
l1=0
l2=0
max1=0
max2=0
for i in range(r):
    s1,s2=map(int,input().split())
    l1+=s1
    l2+=s2
    if ((l1-l2)>max1):
        max1=(l1-l2)
    elif((l2-l1)>max2):
        max2=(l2-l1)
if(max1>max2):
    print("1 "+str(max1))
else:
    print("2 "+str(max2))