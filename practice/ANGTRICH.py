a,b,c=map(int,input().split(" "))
sum=abs(a+b+c)
if sum==180 and (abs(a)>0 and abs(b)>0 and abs(a)>0):
    print('YES')
else:
    print('No')