t=int(input())
j=1
while(j<=t):
    L=int(input())

    num = list(map(int, input().split()))
    num_sum=0

    for i in reversed(range(L)):
        print(num[i],end=" ")

    print()

    for i in range(0,L):
        if i%3==0 and i!=0:        
            print(num[i]+3,end=" ")

    print()

    for i in range(0,L):
        if i%5==0 and i!=0:
            print(num[i]-7,end=" ")

    print()

    for i in range(0,L):
        if i>=3 and i<=7:
            num_sum+=num[i]
    print(num_sum)
    j+=1