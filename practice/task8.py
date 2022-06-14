L=int(input())
num=[]

num = list(map(int, input().split()))

for i in range(L,0,-1):
    print(num[i],end="")


for i in range(0,L):
    if i%3==0:        
        print(num[i]+3)

    if i%5==0:
        print(num[i]-7)

    if i>=3 or i<=7:
        sum+=num[i]
print(sum)