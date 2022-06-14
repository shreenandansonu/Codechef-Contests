t=int(input())
for i in range(0,t,1):
    num=str(input())
    print(int(num[slice(-1,-len(num)-1,-1)]))
