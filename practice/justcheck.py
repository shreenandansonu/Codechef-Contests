N = int(input())
max1 = 0
max2 = 0
x11 = 0
x22 = 0

for i in range(N):
    x1,x2 = map(int,input().split())
    x11+=x1
    x22+=x2

    if((x11-x22)>max1):
        max1 = x11-x22

    elif((x22-x11)>max2):
        max2 = x22-x11

if(max2>max1):
    print('2',max2)
else:
    print('1',max1)