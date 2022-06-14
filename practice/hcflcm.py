import math


for _ in range(int(input())):
   lst=list(map(int,input().split(' ')))
   lst.sort()
   a,b=lst[0],lst[1]
   for i in range(1,math.floor(b/a)+1):
      if (a*i)/b==0:
         LCM=a*i